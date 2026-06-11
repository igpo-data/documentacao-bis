import streamlit as st
import pandas as pd
import streamlit.components.v1 as components


def render():
    st.set_page_config(layout="wide")

    st.markdown("""
    <style>
        .main-title {
            font-size: 34px;
            font-weight: 700;
            color: #1F2937;
            margin-bottom: 4px;
        }

        .subtitle {
            font-size: 15px;
            color: #6B7280;
            margin-bottom: 24px;
        }

        .section-card {
            background-color: #FFFFFF;
            border: 1px solid #E5E7EB;
            border-radius: 14px;
            padding: 22px;
            margin-bottom: 18px;
            box-shadow: 0 2px 10px rgba(31, 41, 55, 0.05);
        }

        .section-title {
            font-size: 21px;
            font-weight: 700;
            color: #111827;
            margin-bottom: 10px;
        }

        .small-label {
            font-size: 13px;
            font-weight: 700;
            color: #374151;
            text-transform: uppercase;
            letter-spacing: 0.04em;
            margin-bottom: 6px;
        }

        .highlight {
            background-color: #F3F4F6;
            border-left: 4px solid #374151;
            padding: 14px 18px;
            border-radius: 10px;
            color: #1F2937;
            margin: 12px 0;
        }

        .metric-box {
            background-color: #F9FAFB;
            border: 1px solid #E5E7EB;
            border-radius: 12px;
            padding: 18px;
            height: 120px;
        }

        .metric-title {
            font-size: 13px;
            color: #6B7280;
            font-weight: 600;
        }

        .metric-value {
            font-size: 24px;
            color: #111827;
            font-weight: 750;
            margin-top: 10px;
        }

        code {
            border-radius: 8px;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="main-title">Situação Coletas</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">Documentação técnica e funcional do fluxo de situação de coletas.</div>',
        unsafe_allow_html=True
    )

    abas = st.tabs([
        "Visão geral",
        "Fluxo de dados",
        "Campos e modelagem",
        "Regras de negócio",
        "Indicadores",
        "Script técnico",
        "Observações"
    ])

    with abas[0]:
        st.markdown("""
        <div class="section-card">
            <div class="section-title">Objetivo do BI</div>
            <p>
            O BI de Situação Coletas tem como objetivo acompanhar as coletas registradas no ambiente,
            avaliando a situação operacional, o prazo previsto de coleta, a data/hora de inclusão, a unidade emissora,
            o remetente, o pagador, o destino, os dados da carga e a classificação final do prazo.
            </p>

            
            O principal foco analítico é identificar se a coleta foi finalizada no prazo ou fora do prazo,
            considerando regras específicas para a unidade SAO, horário de inclusão e calendário de dias úteis.
        
        </div>
        """, unsafe_allow_html=True)

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.markdown("""
            <div class="metric-box">
                <div class="metric-title">Grão da tabela fato</div>
                <div class="metric-value">1 linha por coleta</div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="metric-box">
                <div class="metric-title">Carga</div>
                <div class="metric-value">Incremental</div>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown("""
            <div class="metric-box">
                <div class="metric-title">Origem</div>
                <div class="metric-value">Base 103 SSW</div>
            </div>
            """, unsafe_allow_html=True)

        with col4:
            st.markdown("""
            <div class="metric-box">
                <div class="metric-title">Regra principal</div>
                <div class="metric-value">Prazo coleta</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
        <div class="section-card">
            <div class="section-title">Resumo executivo</div>
            <p>
            O script lê apenas registros alterados ou inseridos na tabela Silver, calcula campos auxiliares de horário,
            ajusta a previsão de coleta conforme regra de unidade e calendário, relaciona as informações com dimensões
            de empresa, período, unidade, remetente e pagador, e entrega uma tabela analítica preparada para consumo no
            modelo semântico do Power BI.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with abas[1]:
        st.markdown('<div class="section-card"><div class="section-title">Fluxo lógico do processo</div>', unsafe_allow_html=True)

        components.html("""
        <div class="mermaid">
        flowchart LR
            A[Tabela Silver Cranilog] --> B[Delta History]
            B --> C[Última versão válida]
            C --> D[table_changes]
            D --> E[Filtra insert e update_postimage]
            E --> F[CTE cte_SituacaoColeta_load]
            F --> G[Classifica horário SAO]
            G --> H[Ajusta previsão de coleta]
            H --> I[Consulta dim_PeriodoAutorizacao]
            I --> J[Calcula próxima data útil]
            J --> K[CTE cte_SituacaoColeta]
            K --> L[Join com dimensões]
            L --> M[Tabela fato de situação de coletas]
            M --> N[Modelo semântico Power BI]
        </div>

        <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
        mermaid.initialize({ startOnLoad: true, theme: 'base' });
        </script>
        """, height=520)

        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("""
        <div class="section-card">
            <div class="section-title">Descrição do fluxo</div>
            <p>
            Primeiro, o script consulta o histórico da tabela Delta para descobrir a última versão válida.
            Depois, usa <strong>table_changes</strong> para carregar somente os registros que foram inseridos
            ou atualizados. Em seguida, cria uma camada intermediária com regras de horário, previsão ajustada
            e cálculo de data útil. Por fim, faz relacionamento com dimensões e gera os campos finais para análise.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with abas[2]:
        st.markdown('<div class="section-card"><div class="section-title">Principais campos do modelo</div>', unsafe_allow_html=True)

        tabela_campos = pd.DataFrame({
            "Campo": [
                "num_NumeroColeta",
                "qtd_Coleta",
                "dat_DataHoraInclusaoColeta",
                "hora_inclusao",
                "dat_DataHoraPrevisaoColetaInicio_SSW",
                "dat_DataHoraPrevisaoColetaInicio",
                "dat_DataHoraPrevisaoColetaFim",
                "dat_DataHoraColetado",
                "qtd_DiasPrazoColeta",
                "nom_Situacao",
                "nom_StatusHorario",
                "nom_PrazoColetaFinalizada",
                "nom_PrazoColeta",
                "id_Empresa",
                "id_PeriodoInclusao",
                "id_PeriodoPrevisaoColeta",
                "id_UnidadeEmissora",
                "id_Remetente",
                "id_Pagador"
            ],
            "Descrição": [
                "Número identificador da coleta.",
                "Contador fixo igual a 1 para permitir agregação de quantidade de coletas.",
                "Data e hora em que a coleta foi incluída.",
                "Coluna mantida para carga incremental no modelo semântico. Não remover.",
                "Previsão original vinda do SSW/Cranilog.",
                "Previsão ajustada pela regra de calendário e horário.",
                "Data e hora final prevista para coleta.",
                "Data e hora em que a coleta foi efetivamente realizada.",
                "Diferença entre data coletada e data prevista.",
                "Situação operacional da coleta.",
                "Classificação da coleta conforme unidade e horário.",
                "Classificação final entre No Prazo e Fora do Prazo.",
                "Classificação de prazo com tratamento específico para SAO e demais filiais.",
                "Chave da dimensão empresa.",
                "Chave da dimensão período de inclusão.",
                "Chave da dimensão período de previsão de coleta.",
                "Chave da dimensão unidade emissora.",
                "Chave da dimensão remetente.",
                "Chave da dimensão pagador."
            ]
        })

        st.dataframe(tabela_campos, use_container_width=True, hide_index=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="section-card"><div class="section-title">Modelagem simplificada</div>', unsafe_allow_html=True)

        components.html("""
        <div class="mermaid">
        erDiagram
            FT_SITUACAO_COLETAS {
                int id_Empresa FK
                int id_PeriodoInclusao FK
                int id_PeriodoPrevisaoColeta FK
                int id_UnidadeEmissora FK
                int id_Remetente FK
                int id_Pagador FK
                string num_NumeroColeta
                int qtd_Coleta
                timestamp dat_DataHoraInclusaoColeta
                timestamp dat_DataHoraPrevisaoColetaInicio
                timestamp dat_DataHoraColetado
                string nom_PrazoColetaFinalizada
                string nom_StatusHorario
            }

            DIM_EMPRESA {
                int id_Empresa PK
                string nom_Empresa
            }

            DIM_PERIODO {
                int id_Periodo PK
                date Data
                date proxima_DataUtil
            }

            DIM_UNIDADE_EMISSORA {
                int id_UnidadeEmissora PK
                string cod_Unidade
            }

            DIM_REMETENTE {
                int id_Remetente PK
                string num_CNPJRemetente
                string nom_ClienteRemetente
            }

            DIM_PAGADOR {
                int id_Pagador PK
                string num_CNPJPagador
                string nom_Pagador
            }

            DIM_EMPRESA ||--o{ FT_SITUACAO_COLETAS : empresa
            DIM_PERIODO ||--o{ FT_SITUACAO_COLETAS : periodo_inclusao
            DIM_PERIODO ||--o{ FT_SITUACAO_COLETAS : periodo_previsao
            DIM_UNIDADE_EMISSORA ||--o{ FT_SITUACAO_COLETAS : unidade
            DIM_REMETENTE ||--o{ FT_SITUACAO_COLETAS : remetente
            DIM_PAGADOR ||--o{ FT_SITUACAO_COLETAS : pagador
        </div>

        <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
        mermaid.initialize({ startOnLoad: true, theme: 'base' });
        </script>
        """, height=720)

        st.markdown("</div>", unsafe_allow_html=True)

    with abas[3]:
        st.markdown('<div class="section-card"><div class="section-title">Regras de negócio</div>', unsafe_allow_html=True)

        with st.expander("Regra 1 — Carga incremental"):
            st.write("""
            O script não carrega a tabela inteira. Ele consulta o histórico Delta, identifica a última versão válida
            e usa table_changes para capturar somente registros inseridos ou atualizados.
            São considerados apenas os registros com _change_type igual a insert ou update_postimage.
            """)

        with st.expander("Regra 2 — Status de horário da unidade SAO"):
            st.write("""
            A unidade SAO possui uma regra específica. Se a cidade remetente estiver entre DIADEMA, BARUERI,
            OSASCO, SAO BERNARDO DO CAMPO, GUARULHOS ou SAO PAULO, o script verifica se a inclusão ocorreu
            até 13:00. Quando isso acontece, a coleta recebe o status SAO - Até as 13hrs. Caso contrário, recebe
            SAO - Após as 13hrs.
            """)

        with st.expander("Regra 3 — Demais filiais"):
            st.write("""
            Quando a unidade é diferente de SAO, o status de horário é classificado como Demais Filiais.
            Essa regra separa a análise operacional de SAO das demais unidades.
            """)

        with st.expander("Regra 4 — Previsão de coleta ajustada"):
            st.write("""
            Quando a previsão inicial está vazia, o script usa a previsão final como base.
            Quando a previsão inicial existe, ela é mantida como referência principal.
            Essa regra evita perda de cálculo quando o campo inicial não vem preenchido.
            """)

        with st.expander("Regra 5 — Próxima data útil"):
            st.write("""
            O script consulta a dimensão dim_PeriodoAutorizacao para buscar a próxima data útil.
            Para SAO após as 13h, quando a data de inclusão é igual à primeira previsão,
            a regra empurra a previsão para a próxima data útil do dia seguinte.
            """)

        with st.expander("Regra 6 — Prazo da coleta finalizada"):
            st.write("""
            Se a situação da coleta for diferente de COLETADA, a coleta é classificada como Fora do Prazo.
            Se estiver coletada e a diferença entre data coletada e data prevista for menor que 1,
            é classificada como No Prazo. Caso contrário, fica Fora do Prazo.
            """)

        st.markdown("</div>", unsafe_allow_html=True)

    with abas[4]:
        st.markdown('<div class="section-card"><div class="section-title">Indicadores sugeridos para o BI</div>', unsafe_allow_html=True)

        tabela_indicadores = pd.DataFrame({
            "Indicador": [
                "Quantidade de Coletas",
                "Coletas no Prazo",
                "Coletas Fora do Prazo",
                "Percentual no Prazo",
                "Percentual Fora do Prazo",
                "Peso Real Total",
                "Peso Cálculo Total",
                "Cubagem Total",
                "Volumes Totais",
                "Valor de Mercadoria",
                "Média de Dias de Prazo"
            ],
            "Regra": [
                "Soma de qtd_Coleta.",
                "Contagem de coletas com nom_PrazoColetaFinalizada = No Prazo.",
                "Contagem de coletas com nom_PrazoColetaFinalizada = Fora do Prazo.",
                "Coletas no Prazo dividido pelo total de coletas.",
                "Coletas fora do prazo dividido pelo total de coletas.",
                "Soma de kgs_PesoRealKG.",
                "Soma de kgs_PesoCalculoKG.",
                "Soma de kgs_CubagemM3.",
                "Soma de qtd_QuantidadeVolume.",
                "Soma de vlr_ValorMercadoria.",
                "Média de qtd_DiasPrazoColeta."
            ]
        })

        st.dataframe(tabela_indicadores, use_container_width=True, hide_index=True)

        st.markdown('<div class="small-label">Medidas DAX sugeridas</div>', unsafe_allow_html=True)

        with st.expander("Quantidade de Coletas"):
            st.code("""
Quantidade Coletas =
SUM(ft_SituacaoColetas[qtd_Coleta])
""", language="DAX")

        with st.expander("Coletas no Prazo"):
            st.code("""
Coletas no Prazo =
CALCULATE(
    [Quantidade Coletas],
    ft_SituacaoColetas[nom_PrazoColetaFinalizada] = "No Prazo"
)
""", language="DAX")

        with st.expander("Coletas Fora do Prazo"):
            st.code("""
Coletas Fora do Prazo =
CALCULATE(
    [Quantidade Coletas],
    ft_SituacaoColetas[nom_PrazoColetaFinalizada] = "Fora do Prazo"
)
""", language="DAX")

        with st.expander("Percentual no Prazo"):
            st.code("""
% Coletas no Prazo =
DIVIDE(
    [Coletas no Prazo],
    [Quantidade Coletas],
    0
)
""", language="DAX")

        st.markdown("</div>", unsafe_allow_html=True)

    with abas[5]:
        st.markdown('<div class="section-card"><div class="section-title">Trechos técnicos documentados</div>', unsafe_allow_html=True)

        with st.expander("Identificação da última versão Delta"):
            st.code("""
from delta.tables import *

last_version = str(
    DeltaTable.forName(spark, f'{table_name_silver}')
    .history()
    .filter("operation IN ('CREATE OR REPLACE TABLE AS SELECT', 'WRITE', 'MERGE', 'UPDATE', 'INSERT')")
    .head()["version"]
)
""", language="python")

        with st.expander("Carga incremental com table_changes"):
            st.code("""
FROM table_changes('{table_name_silver}', {last_version}) AS tempSituacaoColeta
WHERE _change_type IN ('update_postimage', 'insert')
""", language="sql")

        with st.expander("Regra do status de horário"):
            st.code("""
CASE
    WHEN cod_Unidade <> 'SAO' THEN 'Demais Filiais'
    WHEN tempSituacaoColeta.nom_CidadeRemetente IN (
        'DIADEMA',
        'BARUERI',
        'OSASCO',
        'SAO BERNARDO DO CAMPO',
        'GUARULHOS',
        'SAO PAULO'
    )
    THEN CASE
        WHEN CAST(date_format(date_add(HOUR, +3, dat_DataHoraInclusaoColeta), 'HH:mm:ss') AS timestamp)
             <= timestamp('13:00:00')
        THEN 'SAO - Até as 13hrs'
        ELSE 'SAO - Após as 13hrs'
    END
    ELSE 'SAO - Após as 13hrs'
END AS nom_StatusHorario
""", language="sql")

        with st.expander("Regra de previsão ajustada"):
            st.code("""
CASE
    WHEN dat_DataHoraPrevisaoColetaInicio IS NULL
    THEN dat_DataHoraPrevisaoColetaFim
    ELSE dat_DataHoraPrevisaoColetaInicio
END AS dat_DataHoraPrevisaoColetaInicioAjuste
""", language="sql")

        with st.expander("Regra de prazo final"):
            st.code("""
CASE
    WHEN tempSituacaoColeta.nom_Situacao <> 'COLETADA' THEN 'Fora do Prazo'
    WHEN DATE_DIFF(dat_DataHoraColetado, dat_DataPrevisaoColeta) < 1 THEN 'No Prazo'
    ELSE 'Fora do Prazo'
END AS nom_PrazoColetaFinalizada
""", language="sql")

        st.markdown("</div>", unsafe_allow_html=True)

    with abas[6]:
        st.markdown("""
        <div class="section-card">
            <div class="section-title">Pontos de atenção</div>

            <div class="highlight">
            A coluna <strong>hora_inclusao</strong> não deve ser removida, pois o próprio script informa que ela é usada
            na carga incremental do modelo semântico.
            </div>

            <p>
            Também é importante validar se a dimensão <strong>dim_PeriodoAutorizacao</strong> está corretamente atualizada,
            pois ela é responsável pela próxima data útil usada na regra de previsão da coleta.
            </p>

            <p>
            Outro ponto sensível é a regra da unidade SAO após as 13h. Ela altera a data de previsão quando a inclusão
            ocorre no mesmo dia da primeira previsão, jogando a coleta para a próxima data útil.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.text_area(
            "Anotações técnicas",
            "Pendências, validações futuras, prints do BI, ajustes de regra ou dúvidas do time operacional."
        )