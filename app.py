import importlib

import streamlit as st


st.set_page_config(
    page_title="Documentação de Dados e BIs",
    layout="wide",
)


BI_OPTIONS = [
    "Comercial Geral",
    "Acompanhamento Comercial",
    "Análise DFSA",
    "Anomalias e Cancelamentos",
    "Comprovante de Entrega",
    "Contas a Pagar",
    "Contas a Receber",
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
    "Coletas",
]

# Módulos de documentação que já existem no projeto.
BI_MODULES = {
    "Comercial Geral": "pages_bi.bi_Comercial_Geral",
    "Analise Churn": "pages_bi.analise_churn",
    "Anomalias e Cancelamentos": "pages_bi.Anomalias",
    "Cotação": "pages_bi.cotacao",
    "Descarga": "pages_bi.Descarga",
    "E-commerce": "pages_bi.Ecommerce",
    "Embarques": "pages_bi.embarque",
    "Faturamento Interno": "pages_bi.Financeiro2024",
    "Indenização": "pages_bi.indenizacao",
    "Performance Geral": "pages_bi.Performance_Geral",
    "Situação Coleta": "pages_bi.coleta",
    "Coletas": "pages_bi.coleta",
    "SuperAção": "pages_bi.EmissoesAntecipadas",
    "modelo": "pages_bi.modelo",
}


st.sidebar.title("Documentação")
area = st.sidebar.radio(
    "Área",
    ["Banco de dados", "BI's"],
)

search_term = st.text_input(
    "Pesquisar",
    placeholder="Digite o nome de um BI ou procedure...",
).strip()

if area == "Banco de dados":
    from pages_database import procedures

    procedures.render(search_term)
else:
    filtered_bis = [
        bi for bi in BI_OPTIONS if search_term.casefold() in bi.casefold()
    ]

    if not filtered_bis:
        st.info("Nenhum BI encontrado com esse nome.")
    else:
        bi = st.sidebar.radio("BI", filtered_bis)
        module_name = BI_MODULES.get(bi)

        if module_name:
            importlib.import_module(module_name).render()
        elif bi == "Acompanhamento Comercial":
            st.info("Esse BI está dentro do Visão Geral, em uma de suas páginas.")
        else:
            st.title(bi)
            st.info("Documentação em construção.")
