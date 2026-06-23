import pandas as pd
import streamlit as st


UPDATE_PROCEDURES = [
    {
        "Procedure": "atualizar_dim_frete",
        "Finalidade": "Monta e atualiza a dimensão de fretes.",
    },
    {
        "Procedure": "atualizar_dim_frete_updated",
        "Finalidade": "Versão mais recente da atualização da dimensão de fretes.",
    },
    {
        "Procedure": "atualizar_dim_cliente",
        "Finalidade": "Monta e atualiza a dimensão de clientes.",
    },
]

DEDUPLICATION_PROCEDURES = [
    {
        "Procedure": "proc_deletar_duplicada_dim_frete",
        "Finalidade": "Remove registros duplicados da dimensão de fretes.",
    }
]


def _render_procedure_list(procedures: list[dict[str, str]]) -> None:
    st.dataframe(
        pd.DataFrame(procedures),
        use_container_width=True,
        hide_index=True,
    )

    for procedure in procedures:
        with st.expander(procedure["Procedure"]):
            st.write(procedure["Finalidade"])
            st.caption(
                "Inclua aqui as tabelas de origem e destino, regras, periodicidade "
                "de execução e o código SQL da procedure."
            )


def render() -> None:
    st.title("Banco de dados")
    st.write("Documentação das procedures utilizadas nas rotinas de dados.")

    update_tab, deduplication_tab = st.tabs(
        ["Procedures de atualização", "Procedures de remoção de duplicadas"]
    )

    with update_tab:
        st.header("Procedures de atualização")
        _render_procedure_list(UPDATE_PROCEDURES)

    with deduplication_tab:
        st.header("Procedures de remoção de duplicadas")
        _render_procedure_list(DEDUPLICATION_PROCEDURES)
