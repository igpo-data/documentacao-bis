import streamlit as st
import pandas as pd
import streamlit.components.v1 as components


def render():
    st.title("Emissões Antecipadas")

    st.info("""
    Este BI tem por finalidade o calculo do Prêmio Superação
            \n 
            Base: 915 e 206. 
    """)

    abas = st.tabs([
        "Modo de Extração/ Dados",
        "BI"
    ])
    
    with abas[0]:
        st.markdown("""
                            <h5>Modo de extração</h5>""", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)

        with col1:
                st.image("img/Tela206.jpg", caption="Tela de Extração da 206", use_container_width=True)

        with col2:
            st.image("img/Tela915.jpg", caption="Tela de Extração da 915 ", use_container_width=True)
        
        st.markdown("""**Obs**: A tela de extração da 915 muda momentaneamente, sendo o formato de tela como o da imagem, contendo a opção tipo de dados: CTRC e Fatura. 
                    \n 
                    Outro Ponto, a extração da tabela 915 é feita pelo Período de Autorização com o periodo máximo de 31 dias e se preenche quando se escolhe CTRC's
                    em Tipo de Dados.  
                            """)

        st.markdown("""
                            <h5>Dados Brutos.</h5>""", unsafe_allow_html=True)
        
        st.markdown("""**Mapeamento da 206** """)
        tabela206 = pd.DataFrame({
            " Nome ": [
                "NF-E",
                "CHAVE DANFE",
                "XML",
                "NR1/NR2",
                "CTR",
            ],
            "Descrição": [
                "Número da Nota Fiscal.",
                "Chave pode ser copiada com Ctrl-V e colada com Ctrl-C na opção 004 para gerar o CT-e correspondente.",
                "O S indica que o XML da DANFE está disponível, o que facilita a geração do CT-e.",
                "Etiquetas sequenciais dos volumes coletados utilizadas para descarregamento com SSWBar.",
                "S indica que no momento da geração do relatório o pré-CTRC já se encontra emitido.",
            ],
        })
        st.dataframe(tabela206, use_container_width=True, hide_index=True)

        st.markdown("""**Mapeamento da 915** """)
        tabela915 = pd.DataFrame({
            " Nome ": [
                "sigla_ctrc",
                "numero_ctrc",
                "data_emissao",
                "hora_emissao",
                "nro_chave_acesso_cte",
            ],
            "Descrição": [
                "Sigla do CTRC emitido.",
                "Número do CTRC emitido.",
                "Data de emissão do CTRC.",
                "Hora de emissão do CTRC.",
                "Chave de acesso do CT-e/NF-e retornada pela base 915.",
            ],
        })
        st.dataframe(tabela915, use_container_width=True, hide_index=True)

        components.html("""
        <div class="mermaid">
        erDiagram
            VW_206 {
                int id PK
                string veiculo
                numeric motorista
                time hora
                int coleta
                string cnpj_remetente
                text remetente
                int nf_e
                string chave_danfe
                text xml
                text nr1
                text nr2
                text ctr
            }

            VIEW_915 {
                int id PK
                string sigla_ctrc
                string numero_ctrc
                string sigla_cte
                string numero_cte
                string nro_chave_acesso_cte
                date data_emissao
                time hora_emissao
                date data_autorizacao
                time hora_autorizacao
                string situacao_ctrc
                string uf_destino
                string cidade_destino
            }

            VW_206 ||--o{ VIEW_915 : id_danfe_nfe
        </div>

        <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';

        mermaid.initialize({
            startOnLoad: true,
            theme: 'default',
            securityLevel: 'loose'
        });
        </script>
        """, height=900)
    with abas[1]:
        #st.header("Titulo Grandão")

        st.markdown("""
                            <h5>Power Query:</h5>""", unsafe_allow_html=True)

        st.markdown("**Mapeamento das colunas da consulta**")
        tabela_power_query = pd.DataFrame({
            "Coluna": [
                "Data Arquivo",
                "CHAVE DANFE - Copiar",
                "NF-E - Copiar",
                "id_danfe_nfe",
                "915.ctrc",
                "915.data_emissao",
                "915.hora_emissao",
                "915.nro_chave_acesso_nfe",
                "hora_emissao",
                "grupo_hora_emissao",
                "chave_danfe_2",
                "id_ctrc_busca",
            ],
            "Descrição": [
                "Data do arquivo processado. Utilizada para aplicação do filtro incremental através dos parâmetros RangeStart e RangeEnd.",
                "Cópia da coluna CHAVE DANFE criada para permitir a construção de chaves auxiliares sem alterar o campo original.",
                "Cópia da coluna NF-E utilizada na composição da chave de relacionamento com a base 915.",
                "Chave composta pela concatenação da CHAVE DANFE e da NF-E. Utilizada para relacionar os registros da vw_206 com a view_915.",
                "Número do CTRC retornado da view_915 após o relacionamento entre as tabelas.",
                "Data de emissão do CTRC obtida na view_915.",
                "Horário de emissão do CTRC obtido na view_915.",
                "Chave de acesso da Nota Fiscal Eletrônica retornada pela view_915.",
                "Campo derivado do horário de emissão, utilizado para análises e classificações por horário.",
                "Classificação do horário de emissão em faixas de horário para análise operacional.",
                "Campo contendo os primeiros 44 caracteres da chave DANFE. Utilizado para padronização e validações.",
                "Chave técnica criada pela concatenação da CHAVE DANFE, NR1, NR2, COLETA e HORA. Utilizada para identificação única e rastreabilidade dos registros.",
            ],
        })
        st.dataframe(tabela_power_query, use_container_width=True, hide_index=True)

        col_regras, col_chave = st.columns(2)

        with col_regras:
            st.markdown("**Detalhamento do campo `grupo_hora_emissao`**")
            tabela_grupo_hora = pd.DataFrame({
                "Valor": [
                    "Menor que 19hs",
                    "Maior que 19hs",
                    "Vazio",
                ],
                "Regra": [
                    "Horário de emissão menor ou igual ao horário limite definido para antecipação.",
                    "Horário de emissão superior ao horário limite definido para antecipação.",
                    "Registro sem horário de emissão informado.",
                ],
            })
            st.dataframe(tabela_grupo_hora, use_container_width=True, hide_index=True)

        with col_chave:
            st.markdown("**Detalhamento do campo `id_ctrc_busca`**")
            tabela_id_ctrc = pd.DataFrame({
                "Campo utilizado": [
                    "CHAVE DANFE",
                    "NR1",
                    "NR2",
                    "COLETA",
                    "HORA",
                ],
                "Finalidade": [
                    "Identificação da NF-e",
                    "Número de referência operacional",
                    "Número complementar de referência",
                    "Identificador da coleta",
                    "Horário do registro operacional",
                ],
            })
            st.dataframe(tabela_id_ctrc, use_container_width=True, hide_index=True)

        with st.container(border=True):
            st.markdown("""
            A extração dos dados é realizada a partir do banco PostgreSQL,
            utilizando conexão ODBC com o ambiente corporativo da Carvalima.
            A origem da consulta é a view **vw_206**, localizada no schema **public**.
            """)

            col1, col2 = st.columns(2)

            with col1:
                with st.container(border=True):
                    st.markdown("**1. Filtro e padronização inicial**")
                    st.markdown("""
                    Os registros são filtrados por `RangeStart` e `RangeEnd`.
                    Depois, a coluna `Data Arquivo` é convertida para data,
                    garantindo consistência para análises temporais.
                    """)

                with st.container(border=True):
                    st.markdown("**3. Enriquecimento com a view 915**")
                    st.markdown("""
                    É realizado um **Left Join** com a `view_915`, relacionando
                    `id_danfe_nfe` com `id_chave_nota_fiscal`.

                    Informações incorporadas:

                    - CTRC emitido
                    - Data e hora de emissão
                    - Chave de acesso da NF-e
                    """)

                with st.container(border=True):
                    st.markdown("**5. Padronização da chave DANFE**")
                    st.markdown("""
                    A coluna `chave_danfe_2` recebe os primeiros 44 caracteres da
                    chave DANFE, facilitando validações e cruzamentos futuros.
                    """)

            with col2:
                with st.container(border=True):
                    st.markdown("**2. Chave de integração**")
                    st.markdown("""
                    São criadas cópias das colunas `CHAVE DANFE` e `NF-E` para
                    formar a chave `id_danfe_nfe`, usada no relacionamento entre
                    as views 206 e 915.
                    """)

                with st.container(border=True):
                    st.markdown("**4. Classificação por horário**")
                    st.markdown("""
                    A coluna de hora de emissão é tratada para criar
                    `grupo_hora_emissao`, separando as emissões por faixa horária.

                    Classificações:

                    - Menor que 19hs
                    - Maior que 19hs
                    - Vazio
                    """)

                with st.container(border=True):
                    st.markdown("**6. Chave técnica operacional**")
                    st.markdown("""
                    A chave `id_ctrc_busca` identifica cada ocorrência operacional
                    a partir da concatenação dos campos:

                    - CHAVE DANFE
                    - NR1
                    - NR2
                    - COLETA
                    - HORA
                    """)

            st.info(
                "Essa estrutura apoia validações, rastreabilidade e análises de "
                "consistência dos dados dentro do modelo."
            )
