import streamlit as st


UPDATE_PROCEDURES = [
    (
        "atualizar_455_financeiro()",
        "ft_455, ssw_op455, ssw_op455_complementar, dim_frete_455, "
        "dim_frete_compl, dim_cliente, dim_tempo, dim_unidade",
        "Recria a fato financeira da OP455 com dados de frete, mercadoria, "
        "volumes, datas, clientes e unidades.",
    ),
    (
        "atualizar_dim_002_cotacao(carga)",
        "dim_002, ssw_op002",
        "Atualiza a dimensão de cotações, podendo fazer carga total ou incremental.",
    ),
    (
        "atualizar_dim_103(carga)",
        "dim_103, ssw_op103_a",
        "Atualiza a dimensão de coletas com situação, horário, canal de solicitação "
        "e dados operacionais.",
    ),
    (
        "atualizar_dim_200(qtddias)",
        "dim_200, ssw_op200, dim_tempo, dim_horario_descarga",
        "Atualiza manifestos e tempos de descarga da OP200 para um período retroativo.",
    ),
    (
        "atualizar_dim_200BKP(carga)",
        "dim_200, ssw_op200, dim_horario_descarga",
        "Versão backup/antiga da carga da OP200.",
    ),
    (
        "atualizar_dim_441(carga)",
        "dim_441, ssw_op441",
        "Atualiza a dimensão de faturas, cobrança, atraso, prorrogação e liquidação.",
    ),
    (
        "atualizar_dim_915(carga)",
        "dim_915_a_b, ssw_op915_a, ssw_op915_b",
        "Consolida dados da OP915 A e B, ligando CTRC, CT-e e NF-e.",
    ),
    (
        "atualizar_dim_cliente()",
        "dim_cliente, ssw_op467, ssw_op583, ssw_op455",
        "Atualiza o cadastro de clientes usando cadastro oficial, CNPJ principal e "
        "clientes movimentados na OP455.",
    ),
    (
        "atualizar_dim_cliente_bkp()",
        "dim_cliente, ssw_op467, ssw_op583, ssw_op455",
        "Versão backup da carga de clientes.",
    ),
    (
        "atualizar_dim_cliente_teste()",
        "dim_cliente, ssw_op467, ssw_op583, ssw_op455",
        "Versão de teste da carga de clientes, com processamento paginado.",
    ),
    (
        "atualizar_dim_frete(qtddias)",
        "dim_frete, ssw_op455, ssw_op455_complementar, ssw_op200",
        "Atualiza a dimensão de frete com dados comerciais, operacionais, manifestos "
        "e classificações de operação.",
    ),
    (
        "atualizar_dim_frete_bkp(carga)",
        "dim_frete, ssw_op455, ssw_op455_complementar, ssw_op200, dim_tempo",
        "Versão backup da carga da dimensão de frete.",
    ),
    (
        "atualizar_dim_frete_updated(qtddias)",
        "dim_frete, ssw_op455, ssw_op455_complementar, ssw_op200, dim_tempo",
        "Versão atualizada da carga da dimensão de frete usando intervalo retroativo.",
    ),
    (
        "atualizar_dim_pendencia_pi(carga)",
        "dim_pi_pendencia, sacflow_items_compensation_procedure",
        "Atualiza pendências/indenizações vindas do SacFlow.",
    ),
    (
        "atualizar_dim_pi_sacflow(carga)",
        "dim_pi_pendencia, sacflow_items_compensation_procedure",
        "Recarrega a dimensão de pendências PI do SacFlow.",
    ),
    (
        "atualizar_dim_unidade()",
        "dim_unidade, ssw_op455, centros",
        "Atualiza unidades operacionais, regiões, vínculos, UF e cidade.",
    ),
    (
        "atualizar_dimensoes_ft_002(carga)",
        "dim_002, ft_002, ssw_op002",
        "Orquestra a atualização da dimensão e fato da OP002.",
    ),
    (
        "atualizar_ft_915(carga)",
        "ft_915, ssw_op915_a, dim_915_a_b, dim_tempo",
        "Atualiza a fato da OP915 com dados financeiros, pesos, frete e comissões.",
    ),
    (
        "proc_atualizar_chave_cte_cvl_rte_edi_doccob()",
        "rte_base_edi_doccob, ssw_op915_a, ssw_op915_b",
        "Preenche a chave de acesso do CT-e CVL na base RTE/Doccob usando a chave da NF-e.",
    ),
    (
        "sp_atualizar_chave_cte_cvl()",
        "rte_base_edi_doccob, ssw_op915_a, ssw_op915_b",
        "Faz a mesma atualização da chave CT-e CVL na base RTE/Doccob.",
    ),
]

DEDUPLICATION_PROCEDURES = [
    (
        "proc_deletar_duplicada_dim_frete()",
        "dim_frete",
        "Remove registros duplicados da dimensão de fretes.",
    )
]


def _render_procedures(procedures, search_term):
    filtered_procedures = [
        procedure
        for procedure in procedures
        if search_term.casefold() in procedure[0].casefold()
    ]

    if not filtered_procedures:
        st.info("Nenhuma procedure encontrada com esse nome.")
        return

    for name, tables, description in filtered_procedures:
        with st.expander(name):
            st.markdown(f"**Tabelas envolvidas:** {tables}")
            st.markdown(f"**Finalidade:** {description}")


def render():
    st.title("Banco de dados")
    st.write("Documentação das procedures utilizadas nas rotinas de dados.")

    search_term = st.text_input(
        "Pesquisar procedure",
        placeholder="Digite o nome da procedure...",
    ).strip()

    update_tab, deduplication_tab = st.tabs(
        ["Procedures de atualização", "Procedures de remoção de duplicadas"]
    )

    with update_tab:
        _render_procedures(UPDATE_PROCEDURES, search_term)

    with deduplication_tab:
        _render_procedures(DEDUPLICATION_PROCEDURES, search_term)
