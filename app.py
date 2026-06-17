import streamlit as st

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
    from pages_bi import bi_Comercial_Geral
    bi_Comercial_Geral.render()

elif menu == "Analise Churn": 
    from pages_bi import analise_churn
    analise_churn.render() 

elif menu == "Descarga": 
     from pages_bi import Descarga
     Descarga.render() 

elif menu == "Performance Geral": 
     from pages_bi import Performance_Geral
     Performance_Geral.render() 
    
elif menu == "modelo":
    from pages_bi import modelo
    modelo.render()   

elif menu == "E-commerce":
    from pages_bi import Ecommerce
    Ecommerce.render()  

elif menu == "SuperAção":
    from pages_bi import EmissoesAntecipadas
    EmissoesAntecipadas.render() 

elif menu == "Faturamento Interno":
    from pages_bi import Financeiro2024
    Financeiro2024.render() 

elif menu == "Situação Coleta":
    from pages_bi import coleta
    coleta.render() 

elif menu == "Cotação":   st.write("Em construção...")
elif menu == "Faturamento":   st.write("Em construção...")
elif menu == "Anomalias e Cancelamentos":    st.write("Em construção...")
elif menu == "Análise DFSA": st.write("Em construção...")
elif menu == "Torre de Controle":   st.write("Em construção...")
elif menu == "Acompanhamento Comercial":   st.write("Esse BI está dentro do Visão Geral em uma das páginas dele.")
elif menu == "Comprovante de Entrega":   st.write("Em construção...")

   
