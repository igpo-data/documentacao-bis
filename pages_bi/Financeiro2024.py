import streamlit as st
import pandas as pd
import streamlit.components.v1 as components


def render():
    st.title("Faturamento")

    st.info("""
    BI que serve de apuração para o Financeiro, dados advém da 441. 
    """)

    abas = st.tabs([
        "Tela",
        "BI"
    ])

    with abas[0]:
        #st.header("Titulo Grandão")

        st.markdown("""
                    <h5>Visual:</h5>""", unsafe_allow_html=True)
        st.image("img/Financeiro2024.jpg", caption="TVisão da tela de Faturamento", use_container_width=True)

        st.markdown("""
                    <h5>Atualização dos Dados</h5>""", unsafe_allow_html=True)
        st.markdown(""" A rotina de processamento de dados ocorre da seguinte forma: 
            **Mês Vigente**: A atualização de faturas dos documentos emitidos dentro do mês atual é realizada diariamente.     
            **Meses Anteriores**: Para documentos emitidos em meses retroativos (com carga histórica de até 90 dias), a rotina de atualização é executada aos finais de semana. 
            Dessa forma, as informações pendentes serão processadas no final de semana e atualizadas na segunda-feira.  
                     """)
        
  