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
        "Comercial Geral",
        "Acompanhamento Comercial",
        "Análise DFSA",
        "Anomalias e Cancelamentos",
        "Comercial",
        "Comprovante de Entrega", 
        "Contas a Pagar",
        "Contas a Receber",  
        "Comprovante de Entrega", 
        "Controle de Ocorrência",
        "Cotação",
        "Custo de Transferência",
        "Demonstrativo Coleta e Entrega",
        "Descarga",     
        "DRE", 
        "DRE Filiais",
        "DRE PPR",
        "E-commerce",
        "Embarques",
        "Faturamento",
        "Inadimplência - Filial",
        "Indenização",
        "Performance Geral", 
        "Produtividade Comercial",
        "SAC",
        "Situação Coleta",
        "SSW Mobile",
        "Torre de Controle"]
)

if menu == "BI Comercial Geral":
    bi_Comercial_Geral.render()

elif menu == "BI Acompanhamento Comercial":
    bi_Acompanhamento_Comercial.render()

elif menu == "BI Análise DFS":
    bi_Analise_dfsa.render()

