import base64
from pathlib import Path
import streamlit as st
import pandas as pd
import streamlit.components.v1 as components


def img_to_base64(path):
    return base64.b64encode(Path(path).read_bytes()).decode()


def render():
    # Se já tiver st.set_page_config() no app.py, REMOVA esta linha daqui
    # st.set_page_config(layout="wide")

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

        def render_situacao_coleta_interativo():
            imagem = img_to_base64("img/SituacaoColeta.jpg")

            html = f"""
            <style>
                .painel {{
                    position: relative;
                    width: 100%;
                    max-width: 1550px;
                    margin: auto;
                }}

                .painel img {{
                    width: 100%;
                    border-radius: 8px;
                }}

                .hotspot {{
                    position: absolute;
                    cursor: pointer;
                    border: 2px solid transparent;
                    transition: 0.2s;
                }}

                .hotspot:hover {{
                    border: 3px solid #00BFFF;
                    background: rgba(0,191,255,0.15);
                    box-shadow: 0 0 14px rgba(0,191,255,0.8);
                }}

                .tooltip {{
                    visibility: hidden;
                    opacity: 0;
                    position: absolute;
                    z-index: 9999;
                    width: 380px;
                    background: white;
                    color: #333;
                    border-radius: 14px;
                    padding: 16px;
                    box-shadow: 0 8px 24px rgba(0,0,0,0.30);
                    top: 105%;
                    left: 0;
                    transition: opacity 0.25s ease;
                }}

                .hotspot:hover .tooltip {{
                    visibility: visible;
                    opacity: 1;
                }}

                .tooltip h3 {{
                    margin-top: 0;
                    color: #0b4f8a;
                }}
            </style>

            <div class="painel">

                <img src="data:image/png;base64,{imagem}">

                <div class="hotspot" style="left:0.5%; top:20%; width:16%; height:14%;">
                    <div class="tooltip">
                        <h3>Coletas</h3>
                        <p>Quantidade total de coletas registradas no período selecionado.</p>
                    </div>
                </div>

                <div class="hotspot" style="left:17%; top:20%; width:16%; height:14%;">
                    <div class="tooltip">
                        <h3>Coletadas</h3>
                        <p>Quantidade de coletas que possuem data de coleta.</p>
                    </div>
                </div>

                <div class="hotspot" style="left:34%; top:20%; width:16%; height:14%;">
                    <div class="tooltip">
                        <h3>Comandadas</h3>
                        <p>Coletas já encaminhadas operacionalmente para execução.</p>
                    </div>
                </div>

                <div class="hotspot" style="left:50.5%; top:20%; width:16%; height:14%;">
                    <div class="tooltip">
                        <h3>Canceladas</h3>
                        <p>Coletas canceladas antes da conclusão operacional.</p>
                    </div>
                </div>

                <div class="hotspot" style="left:67%; top:20%; width:16%; height:14%;">
                    <div class="tooltip">
                        <h3>Cadastradas</h3>
                        <p>Coletas registradas no sistema e aguardando evolução.</p>
                    </div>
                </div>

                <div class="hotspot" style="left:83.5%; top:20%; width:16%; height:14%;">
                    <div class="tooltip">
                        <h3>Pré-Cadastradas</h3>
                        <p>Coletas que ainda não concluíram o processo completo de cadastro.</p>
                    </div>
                </div>

                <div class="hotspot" style="left:0.5%; top:36%; width:16%; height:14%;">
                    <div class="tooltip">
                        <h3>Hoje</h3>
                        <p>Coletas com vencimento previsto para o dia atual.</p>
                    </div>
                </div>

                <div class="hotspot" style="left:17%; top:36%; width:16%; height:14%;">
                    <div class="tooltip">
                        <h3>A Vencer</h3>
                        <p>Coletas ainda dentro do prazo previsto.</p>
                    </div>
                </div>

                <div class="hotspot" style="left:34%; top:36%; width:16%; height:14%;">
                    <div class="tooltip">
                        <h3>Vencidas</h3>
                        <p>Coletas cuja data prevista já foi ultrapassada.</p>
                    </div>
                </div>

            </div>
            """

            components.html(
                html,
                height=900,
                scrolling=True
            )

        render_situacao_coleta_interativo()

        st.markdown("""
        <div class="section-card">
            <div class="section-title">Objetivo do BI</div>
            <p>
            O BI de Situação Coletas tem como objetivo acompanhar as coletas registradas no ambiente,
            avaliando a situação operacional, o prazo previsto de coleta, a data/hora de inclusão, a unidade emissora,
            o remetente, o pagador, o destino, os dados da carga e a classificação final do prazo.
            </p>

            <p>
            O principal foco analítico é identificar se a coleta foi finalizada no prazo ou fora do prazo,
            considerando regras específicas para a unidade SAO, horário de inclusão e calendário de dias úteis.
            </p>
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
                <div class="diagram-card">
                    <div class="diagram-toolbar">
                        <span>Arraste o diagrama para mover. Use o scroll para zoom.</span>
                        <button id="zoomIn">Aproximar</button>
                        <button id="zoomOut">Afastar</button>
                        <button id="reset">Resetar</button>
                    </div>

                    <div id="diagram-wrapper">
                        <div id="diagram-content">
                            <pre class="mermaid">
                flowchart TB
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
                            </pre>
                        </div>
                    </div>
                </div>

                <style>
                    .diagram-card {
                        width: 100%;
                        height: 850px;
                        border: 1px solid #E5E7EB;
                        border-radius: 14px;
                        background: #FFFFFF;
                        overflow: hidden;
                        box-sizing: border-box;
                    }

                    .diagram-toolbar {
                        height: 48px;
                        display: flex;
                        align-items: center;
                        gap: 10px;
                        padding: 0 14px;
                        border-bottom: 1px solid #E5E7EB;
                        background: #F9FAFB;
                        font-family: Arial, sans-serif;
                        font-size: 13px;
                        color: #374151;
                    }

                    .diagram-toolbar button {
                        border: 1px solid #D1D5DB;
                        background: #FFFFFF;
                        color: #111827;
                        border-radius: 8px;
                        padding: 6px 10px;
                        cursor: pointer;
                        font-size: 12px;
                    }

                    #diagram-wrapper {
                        width: 100%;
                        height: 802px;
                        overflow: hidden;
                        cursor: grab;
                        background:
                            linear-gradient(#F3F4F6 1px, transparent 1px),
                            linear-gradient(90deg, #F3F4F6 1px, transparent 1px);
                        background-size: 24px 24px;
                    }

                    #diagram-content {
                        width: max-content;
                        padding: 60px;
                    }

                    .mermaid svg {
                        max-width: none !important;
                        height: auto !important;
                    }
                </style>

                <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
                <script src="https://cdn.jsdelivr.net/npm/@panzoom/panzoom@4.6.0/dist/panzoom.min.js"></script>

                <script>
                    mermaid.initialize({
                        startOnLoad: true,
                        theme: "base",
                        flowchart: {
                            useMaxWidth: false,
                            htmlLabels: true,
                            curve: "basis"
                        }
                    });

                    setTimeout(function() {
                        const elem = document.getElementById("diagram-content");
                        const wrapper = document.getElementById("diagram-wrapper");

                        const panzoom = Panzoom(elem, {
                            maxScale: 2.5,
                            minScale: 0.4,
                            contain: "outside",
                            startScale: 1
                        });

                        wrapper.addEventListener("wheel", panzoom.zoomWithWheel);

                        document.getElementById("zoomIn").addEventListener("click", function() {
                            panzoom.zoomIn();
                        });

                        document.getElementById("zoomOut").addEventListener("click", function() {
                            panzoom.zoomOut();
                        });

                        document.getElementById("reset").addEventListener("click", function() {
                            panzoom.reset();
                        });
                    }, 800);
                </script>
                """, height=700, scrolling=False)
                        
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
                "Previsão original vinda do SSW.",
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
        st.markdown("""
                    ### 1. Carga Incremental

                    O processo foi desenvolvido utilizando carga incremental através do recurso
                    `table_changes` do Delta Lake. Antes da execução da carga, o script consulta o
                    histórico da tabela da camada Silver para identificar a última versão válida
                    processada. A partir dessa versão, são recuperadas somente as alterações
                    ocorridas desde a última execução, reduzindo o volume de dados processados e
                    otimizando o desempenho da atualização.

                    O Delta Lake mantém um histórico completo das modificações realizadas nos
                    registros, permitindo identificar quais dados foram inseridos, alterados ou
                    removidos ao longo do tempo. Para isso, a função `table_changes` disponibiliza
                    a coluna técnica `_change_type`, responsável por indicar o tipo de alteração
                    realizada em cada registro.

                    Os principais valores possíveis são:

                    | Tipo de Alteração | Descrição |
                    |------------------|-----------|
                    | `insert` | Registro inserido pela primeira vez na tabela. |
                    | `delete` | Registro removido da tabela. |
                    | `update_preimage` | Estado do registro antes da atualização. |
                    | `update_postimage` | Estado do registro após a atualização. |

                    Para a construção da tabela analítica, são considerados apenas os registros
                    classificados como `insert` e `update_postimage`, uma vez que representam,
                    respectivamente, novos registros e a versão mais atualizada dos dados.

                    Dessa forma, o modelo sempre trabalha com o estado mais recente das coletas,
                    evitando o processamento de versões antigas e garantindo maior eficiência na
                    carga incremental.
                    

                    ### 2. Classificação de Horário da Unidade SAO

                    Para as coletas pertencentes à unidade **SAO**, existe uma regra específica de
                    classificação baseada na cidade do remetente e no horário de inclusão da coleta.

                    São consideradas as seguintes cidades:

                    - DIADEMA
                    - BARUERI
                    - OSASCO
                    - SAO BERNARDO DO CAMPO
                    - GUARULHOS
                    - SAO PAULO

                    Quando a coleta for registrada até às **13h00**, ela recebe a classificação:

                    > SAO - Até as 13hrs

                    Quando registrada após esse horário, recebe a classificação:

                    > SAO - Após as 13hrs

                    ---

                    ### 3. Tratamento das Demais Filiais

                    Quando a unidade emissora for diferente de SAO, a coleta não participa da regra
                    especial de horário.

                    Nestes casos o campo **nom_StatusHorario** recebe automaticamente:

                    > Demais Filiais

                    Essa separação permite análises específicas para a operação da filial de São
                    Paulo sem impactar as demais unidades.

                    ---

                    ### 4. Ajuste da Primeira Previsão de Coleta

                    O sistema utiliza prioritariamente a coluna
                    `dat_DataHoraPrevisaoColetaInicio`.

                    Quando essa informação não estiver disponível, a previsão passa a utilizar a
                    coluna:

                    `dat_DataHoraPrevisaoColetaFim`

                    Dessa forma evita-se a perda da informação de previsão durante o processamento
                    dos dados.

                    ---

                    ### 5. Cálculo da Próxima Data Útil

                    A previsão de coleta é recalculada utilizando a dimensão
                    `dim_PeriodoAutorizacao`.

                    Para coletas da unidade SAO classificadas como:

                    > SAO - Após as 13hrs

                    e cuja data de inclusão seja igual à primeira data prevista de coleta, o sistema
                    desloca a previsão para a próxima data útil disponível.

                    Essa regra garante aderência ao processo operacional da unidade.

                    ---

                    ### 6. Validação de Prazo da Coleta

                    A classificação final do prazo da coleta é baseada na situação operacional e na
                    diferença entre a data prevista e a data efetiva da coleta.

                    Critérios utilizados:

                    | Situação | Resultado |
                    |-----------|------------|
                    | Situação diferente de COLETADA | Fora do Prazo |
                    | Coletada com diferença menor que 1 dia | No Prazo |
                    | Coletada com diferença igual ou superior a 1 dia | Fora do Prazo |

                    O resultado é armazenado na coluna:

                    `nom_PrazoColetaFinalizada`

                    ---

                    ### 7. Controle de Vencimento da Coleta

                    O sistema também gera uma classificação para monitoramento operacional das
                    coletas pendentes.

                    Possíveis valores:

                    - Hoje
                    - Vencida
                    - A Vencer
                    - Finalizada

                    Essa informação permite identificar rapidamente coletas que ainda aguardam
                    atendimento ou que já ultrapassaram a data prevista.

                    </div>
                    """, unsafe_allow_html=True)

    with abas[4]:
        st.markdown('<div class="section-card"><div class="section-title">Indicadores</div>', unsafe_allow_html=True)

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
                "Média de Dias de Prazo",
                "Performance",
                "Efetividade"
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
                "Média de qtd_DiasPrazoColeta.",
                "Coletadas/ total de coletas",
                "Coletadas no prazo/ total de coletadas"
            ]
        })

        st.dataframe(tabela_indicadores, use_container_width=True, hide_index=True)

        

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