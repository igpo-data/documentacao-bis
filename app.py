import importlib
import subprocess
from pathlib import Path

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


@st.cache_data(ttl=300)
def get_recent_commit_counts(days):
    counts = {}

    for bi, module_name in BI_MODULES.items():
        module_path = Path(*module_name.split(".")).with_suffix(".py")

        try:
            result = subprocess.run(
                [
                    "git",
                    "log",
                    f"--since={days} days ago",
                    "--format=%H",
                    "--",
                    str(module_path),
                ],
                capture_output=True,
                text=True,
                check=False,
            )
        except Exception:
            counts[bi] = 0
            continue

        if result.returncode != 0:
            counts[bi] = 0
            continue

        counts[bi] = len([line for line in result.stdout.splitlines() if line.strip()])

    return counts


def sort_bis_by_recent_commits(bis, commit_counts):
    return sorted(
        bis,
        key=lambda bi: (-commit_counts.get(bi, 0), bi.casefold()),
    )

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
    sort_mode = st.sidebar.radio(
        "Ordenação dos BI's",
        ["Lista padrão", "Mais comitados recentemente"],
    )

    commit_counts = {}
    if sort_mode == "Mais comitados recentemente":
        commit_days = st.sidebar.slider(
            "Período dos commits",
            min_value=1,
            max_value=60,
            value=14,
            help="Quantidade de dias usada para contar commits por página de BI.",
        )
        commit_counts = get_recent_commit_counts(commit_days)
        bi_options = sort_bis_by_recent_commits(BI_OPTIONS, commit_counts)
        st.sidebar.caption(f"Ordenado pelos commits dos últimos {commit_days} dias.")
    else:
        bi_options = BI_OPTIONS

    filtered_bis = [
        bi for bi in bi_options if search_term.casefold() in bi.casefold()
    ]

    if not filtered_bis:
        st.info("Nenhum BI encontrado com esse nome.")
    else:
        def format_bi_option(bi):
            if sort_mode != "Mais comitados recentemente":
                return bi

            count = commit_counts.get(bi, 0)
            label = "commit" if count == 1 else "commits"
            return f"{bi} ({count} {label})"

        bi = st.sidebar.radio("BI", filtered_bis, format_func=format_bi_option)
        module_name = BI_MODULES.get(bi)

        if module_name:
            importlib.import_module(module_name).render()
        elif bi == "Acompanhamento Comercial":
            st.info("Esse BI está dentro do Visão Geral, em uma de suas páginas.")
        else:
            st.title(bi)
            st.info("Documentação em construção.")
