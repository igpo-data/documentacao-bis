<<<<<<< HEAD
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

st.title("📊 Documentação dos BIs - Carvalima")

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
=======
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
>>>>>>> c288ff076c102e74ddfbd36fe2a1f2cac3b9e6b9
