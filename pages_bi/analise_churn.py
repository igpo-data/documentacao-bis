import streamlit as st
import pandas as pd
import streamlit.components.v1 as components


def render():
    st.title("Análise Churn")

    st.info("""
    Objetivo desse BI é fazer uma ánalise do cliente com base no histórico de faturamento do pagador (CNPJ Principal). 

    """)

    abas = st.tabs([
        "Análise Churn ",
        "Detalhamento "
    ])

    with abas[0]:
    
        st.image(
                "img/Analise Churn.JPG",
                    caption="Tela da Analise Churn",
                    use_container_width=True
                     )


        st.markdown("""
                    <h5> Regra de Negócio – Classificação de Status do Cliente</h5>""", unsafe_allow_html=True)

        st.markdown("""    
            A classificação de status do cliente é realizada com base no histórico mensal de faturamento do pagador (CNPJ Principal), 
            considerando o mês mais recente disponível na base de dados como referência.


            **Clientes Carteira**: Total de clientes. 

            **Ativos**: Cliente que realizou frete no mês atual e mantém recorrência normal de fretes.
                Condição:  Faturou no mês atual e não se enquadra como Novo ou Reconquistado. 

            **Em risco**: São clientes que param há 1 a 3 meses, ou seja, clientes que não realizaram frete no mês atual e seu último frete ocorreu há no máximo 3 meses. 

            **Reconquista**: Cliente que voltou a faturar no mês atual após permanecer mais de 6 meses sem fretes. 
                Condição: Faturou no mês atual, possui histórico anterior e ficou mais de 6 meses sem faturar antes do retorno. 


            **Inativos**: Cliente que está há mais de 12 meses sem realizar fretes.

            **Observações Importantes**\n
            •	A análise é feita por CNPJ Principal do cliente.\n
            •	A referência de “mês atual” corresponde ao mês mais recente existente na base de dados.\n
            •	A classificação considera apenas clientes que possuem histórico de faturamento.\n
            •	O cliente pode mudar de status mensalmente conforme seu comportamento de frete.\n
                     """)
        

        ############################# Detalhamento ###############################
        st.markdown("""
                    <h4>Modelagem de Dados</h4>""", unsafe_allow_html=True)

    with abas[1]:
        st.header("Detalhamento")

       
