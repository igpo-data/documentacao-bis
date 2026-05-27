import streamlit as st
from pages_bi import (
    bi_Comercial_Geral,
    bi_Acompanhamento_Comercial,
    bi_Analise_dfsa
)

st.set_page_config(
    page_title="Documentação dos BIs",
    layout="wide"
)

#st.title("📊 Documentação dos BIs - Carvalima")

menu = st.sidebar.selectbox(
    "Escolha o BI",
    [
        "BI Comercial Geral",
        "BI Acompanhamento Comercial",
        "BI Análise DFS"
    ]
)

if menu == "BI Comercial Geral":
    bi_Comercial_Geral.render()

elif menu == "BI Acompanhamento Comercial":
    bi_Acompanhamento_Comercial.render()

elif menu == "BI Análise DFS":
    bi_Analise_dfsa.render()

