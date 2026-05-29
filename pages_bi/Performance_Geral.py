import streamlit as st
import pandas as pd
import streamlit.components.v1 as components


def render():
    st.title("Performance Geral")

    st.info(""" Performance Geral é um BI que tem como fontes de dados a base 455 (+ complementar B) e 36 do SSW. """)

    abas = st.tabs([
        "Performan Geral - Autorização",
        "Performance Unidade/Cliente - Autorização",
        "Performance Região",
        "Previsão de Entregas - Resumo",
        "Previsão de Entregas - Quadro Geral",
        "Previsão de Entregas - Emissão",
        "Previsão de Unidade/Cliente Emissão",
        "Efetividade de Entregas - Motoristas",
        "Efetividade de Entregas - Evolução",
        "Efetividade de Entregas - Retornados",
        "Efetividade de Entregas - Mensal",
        "Efetividade de Entregas Tipo de Operação e Torre",
        "Efetividade de Entrega - CTEs Romaneados",
        "Performance Prioridade CGB"
    ])

    with abas[0]:
        st.markdown("""
                    <h4>Filtros: </h4>""", unsafe_allow_html=True)
        
        st.markdown("""
      **Período de Autorização** - *dim_PeriodoAutorizacao*: Período que advém da 455.\n
      **Origem:** - *dim_UnidadeEmissora*: Utiliza aqui nom_UnidadeEmissora e nom_VinculoCentro.\n
      **Destino** - *dim_UnidadeReceptora*: Utiliza aqui cod_UnidadeReceptora e nom_VinculoCentro.\n
      **Ocorrência** - *dim_Ocorrencia*: cod_Ocorrência, a qual é constituída pela 455 complementar B. \n
      **Pagador** - *dim_Pagador*: utiliza nom_ClientePagador o qual advém da 455.\n
      **Status** - *fato_FreteExpedidoRecebido*: utiliza a nom_StatusEntregaPendente, o qual é um atributo dentro das tabelas
                    de medidas advindas da 455, as quais há análise dos CTRC com ocorrência 1 (entrega), dentro disso se avalia se foram dentro ou fora do prazo.\n
      **CTRC** - *dim_CTRC*: utiliza a coluna nom_SiglaCTRC, o qual é todos os CTRC’s da tabela 455 durante aquele período filtrado. """)
        
        st.markdown("""
                    <h5>Sistema de Paginação</h5>""", unsafe_allow_html=True)
        
        st.markdown("""Há uma dupla tela uma filtrada por Período de Autorização e outra filtrada por Período de Previsão de Entrega.""")
        
        col1, col2 = st.columns(2)

        with col1:
                st.image("img/Performance_Geral_Autorização.png", caption="Tela filtrada pelo período de Autorização", use_container_width=True)

        with col2:
            st.image("img/Performance_Geral_Previsão_Entrega.png", caption="Tela Filtrada pelo período de Previsão de Entrega ", use_container_width=True)
   
        st.image("img/Performance_Geral-pg.jpg", caption="Sistema de Botões do Painel", use_container_width=True)
    
    
       ########### tabela de exemplo 
        legenda_Bot = pd.DataFrame({

                    " Número ": [
                    "1",
                    "2",
                    "3"
                ],

                "Descrição": [
                    "linha",
                    "linha",
                    "linha"    
                ]})

        st.dataframe(
                    legenda_Bot,
                    use_container_width=True,
                    hide_index=True
                )

        
        components.html("""
                <div class="mermaid">
                erDiagram
                        
                    tabela 1 {
                        numeric coluna 1 
                        int coluna 2
                    }

                      tabela 2 {
                        numeric coluna 1 
                        int coluna 2
                    }

                      tabela 3 {
                        numeric coluna 1 
                        int coluna 2
                    }

                    
                        
                </div>

                <script type="module">
                import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
                mermaid.initialize({ startOnLoad: true });
                </script>
                """, height=800)


        
########------------Visão Geral ------------------########
    with abas[1]:
        st.markdown("""
                    <h4>Visual:</h4>""", unsafe_allow_html=True)
        
        ##### Depois adiciona  diagrama #####
        ##components.html("""
               ##<div class="mermaid">
                ##erDiagram

                   
                    

                    ##dim_PeriodoMetaDiaria ||--o{ fato_MetaUnidadeDiaria : Periodo_Meta
                    ##dim_UnidadeBeneficiaria ||--o{ fato_MetaUnidadeDiaria : Unidade

                    ##dim_PeriodoAutorizacao ||--o{ fato_FreteExpedidoRecebido : PeriodoAut
                    ##dim_PeriodoEmissao ||--o{ fato_FreteExpedidoRecebido : PeriodoEmissao
                    ##dim_UnidadeBeneficiaria ||--o{ fato_FreteExpedidoRecebido : Unidade

                ##</div>

                ##<script type="module">
                ##import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
                ##mermaid.initialize({ startOnLoad: true });
                ##</script>
                ##""", height=800)

        st.markdown("""Neste BI se encontra a quantidade de dias úteis dentro daquele Mês, dessa forma, o 
                    mês de abril há 21 dias úteis tirando os feriados e contabilizando o sabado como 0,25 para fins 
                    de faturamento. 
        """ )

        st.image(
                "img/Comercial_Geral_Visão_Geral_PF.PNG",
                    caption="Tabela de exportação.",
                    use_container_width=True
                     )

        st.table({
            "Fonte": ["tabela_exemplo"],
            "Tipo": ["Tabela PostgreSQL"],
            "Descrição": ["Descrever o uso dessa tabela"]
        })

        st.markdown("""
                    <h4>Modelagem de Dados</h4>""", unsafe_allow_html=True)

    with abas[2]:
        st.header("⚙️ Regras de Negócio")

        with st.expander("Regra 1"):
            st.write("""
            Explique a regra aqui.
            """)

        with st.expander("Regra 2"):
            st.write("""
            Explique outra regra aqui.
            """)

    with abas[3]:
        st.header("📐 Medidas DAX")

        with st.expander("Nome da medida DAX"):
            st.code("""
Medida =
CALCULATE(
    COUNTROWS(tabela),
    tabela[coluna] = "valor"
)
""", language="DAX")

    with abas[4]:
        st.header("🧾 Consultas SQL")

        with st.expander("Consulta principal"):
            st.code("""
SELECT *
FROM public.tabela_exemplo
LIMIT 100;
""", language="sql")

    with abas[5]:
        st.header("🖼️ Imagens do BI")

        st.warning("Coloque o print do BI na pasta img/ e altere o caminho abaixo.")

        # exemplo:
        # st.image("img/bi_descarga.png", caption="Tela principal do BI")

    with abas[6]:
        st.header("📝 Observações")

        st.text_area(
            "Anotações",
            "Pendências, melhorias futuras, dúvidas ou pontos de atenção."
        )