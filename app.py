import streamlit as st
from pages_bi import (
    bi_Comercial_Geral,
    bi_Acompanhamento_Comercial,
    bi_Analise_dfsa,
    modelo,
    analise_churn,
    Descarga,
    Performance_Geral,
    Ecommerce,
    cotacao,
    EmissoesAntecipadas,
    Financeiro2024,
    coleta
    )

st.set_page_config(
    page_title="Documentação dos BIs",
    layout="wide"
)

#st.title("📊 Documentação dos BIs - Carvalima")

menu = st.sidebar.radio(
    "",
    [
        "Comercial Geral",
        "Acompanhamento Comercial",
        "Análise DFSA",
        "Anomalias e Cancelamentos",
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
        "Torre de Controle",
        "Analise Churn",
        "modelo",
        "SuperAção", 
        "Faturamento Interno",
        "Coletas"
        ]
)

if menu == "Comercial Geral":
    bi_Comercial_Geral.render()

elif menu == "Analise Churn": 
    analise_churn.render() 

elif menu == "Descarga": 
     Descarga.render() 

elif menu == "Performance Geral": 
     Performance_Geral.render() 
    
elif menu == "modelo":
    modelo.render()   

elif menu == "E-commerce":
    Ecommerce.render()  

elif menu == "SuperAção":
    EmissoesAntecipadas.render() 

elif menu == "Faturamento Interno":
    Financeiro2024.render() 

elif menu == "Situação Coleta":
    coleta.render() 

elif menu == "Cotação":   st.write("Em construção...")
elif menu == "Faturamento":   st.write("Em construção...")
elif menu == "Anomalias e Cancelamentos":    st.write("Em construção...")
elif menu == "Análise DFSA": st.write("Em construção...")
elif menu == "Torre de Controle":   st.write("Em construção...")
elif menu == "Acompanhamento Comercial":   st.write("Esse BI está dentro do Visão Geral em uma das páginas dele.")
elif menu == "Comprovante de Entrega":   st.write("Em construção...")

   
