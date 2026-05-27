# pages_bi/modelo_bi.py

import streamlit as st

def render():
    st.title("📊 Nome do BI")

    st.info("""
    Descreva aqui o objetivo principal deste BI.
    Exemplo: acompanhar coletas, descargas, faturamento, indenizações etc.
    """)

    abas = st.tabs([
        "📌 Visão Geral",
        "🗂️ Fontes",
        "⚙️ Regras",
        "📐 Medidas DAX",
        "🧾 SQL",
        "🖼️ Imagens",
        "📝 Observações"
    ])

    with abas[0]:
        st.header("📌 Visão Geral")

        st.markdown("""
        **Objetivo do BI:**  
        Explique o que o painel acompanha.

        **Público-alvo:**  
        Exemplo: gestão, qualidade, operacional, financeiro.

        **Principais indicadores:**  
        - Indicador 1
        - Indicador 2
        - Indicador 3
        """)

        col1, col2, col3 = st.columns(3)

        col1.metric("Indicador 1", "0")
        col2.metric("Indicador 2", "0%")
        col3.metric("Indicador 3", "R$ 0,00")

    with abas[1]:
        st.header("🗂️ Fontes de Dados")

        st.markdown("Tabelas, views ou arquivos usados neste BI.")

        st.table({
            "Fonte": ["tabela_exemplo"],
            "Tipo": ["Tabela PostgreSQL"],
            "Descrição": ["Descrever o uso dessa tabela"]
        })

    with abas[2]:
        st.header("⚙️ Regras de Negócio")

        with st.expander("Regra 1"):
            st.write("""
            Explique a regra aqui.
            """)

        with st.expander("Regra 2"):
            st.write("""
            Explique outra regra aqui.
            """)

    with abas[3]:
        st.header("📐 Medidas DAX")

        with st.expander("Nome da medida DAX"):
            st.code("""
Medida =
CALCULATE(
    COUNTROWS(tabela),
    tabela[coluna] = "valor"
)
""", language="DAX")

    with abas[4]:
        st.header("🧾 Consultas SQL")

        with st.expander("Consulta principal"):
            st.code("""
SELECT *
FROM public.tabela_exemplo
LIMIT 100;
""", language="sql")

    with abas[5]:
        st.header("🖼️ Imagens do BI")

        st.warning("Coloque o print do BI na pasta img/ e altere o caminho abaixo.")

        # exemplo:
        # st.image("img/bi_descarga.png", caption="Tela principal do BI")

    with abas[6]:
        st.header("📝 Observações")

        st.text_area(
            "Anotações",
            "Pendências, melhorias futuras, dúvidas ou pontos de atenção."
        )