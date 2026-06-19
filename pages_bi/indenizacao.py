import streamlit as st
import pandas as pd
import streamlit.components.v1 as components


def render():
    st.title("Indenização")

    st.info("""
   BI a ser desenvolvido para acompanhar as indenizações, suas causas, valores e status.
    """)

    abas = st.tabs([
        "aba 1 ",
        "aba 2 ",
        "aba 3 "
    ])

    with abas[0]:
        st.header("Titulo Grandão")

        st.markdown("""
                    <h4>Visual:</h4>""", unsafe_allow_html=True)

#########_____________ Coloca alguma  imagam (Conter img)
       ## st.image(
        ##"img/Acomp_Geral_Principal.PNG",
        ##caption="Tela principal do BI",
        ##use_container_width=True
        ##)
        
        st.markdown("""
      colocar um texto 
                    \n 
                    pular a linha   """)
        
        #--------DEIXA AQUI QUANDO EU PRECISA:: colunas ::::::
        #col1, col2, col3 = st.columns(3)
        #col1.metric("Indicador 1", "0")
        #col2.metric("Indicador 2", "0%")
        #col3.metric("Indicador 3", "R$ 0,00")

    
        
        st.markdown("""
            texto **texto** texto texto texto, 
            texto <span style="background-color:#FFF3B0; padding:2px 6px; border-radius:5px;">
            texto colorido  texto colorido
            </span>, <span style="background-color:#FFF3B0; padding:2px 6px; border-radius:5px;">
             texto colorido
            </span>,<span style="background-color:#FFF3B0; padding:2px 6px; border-radius:5px;">
             texto colorido</span>.
            """, unsafe_allow_html=True)
        

        

       ########### tabela de exemplo 
        tabela = pd.DataFrame({

                    " Titulo Coluna 1  ": [
                    "linha",
                    "linha",
                    "linha"
                ],

                "Titulo Coluna 2": [
                    "linha",
                    "linha",
                    "linha"    
                ],

                "Titulo Coluna 3": [
                    "linha",
                    "linha",
                    "linha"]})

        st.dataframe(
                    tabela,
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