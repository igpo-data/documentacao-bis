import streamlit as st
from pages_bi import bi_faturamento, bi_coletas, bi_descarga, bi_indenizacoes

st.set_page_config(
    page_title="Documentação dos BIs",
    layout="wide"
)

st.title("📊 Documentação dos BIs - Carvalima")

menu = st.sidebar.selectbox(
    "Escolha o BI",
    [
        "BI Faturamento",
        "BI Coletas",
        "BI Descarga",
        "BI Indenizações"
    ]
)

if menu == "BI Faturamento":
    bi_faturamento.render()

elif menu == "BI Coletas":
    bi_coletas.render()

elif menu == "BI Descarga":
    bi_descarga.render()

elif menu == "BI Indenizações":
    bi_indenizacoes.render()