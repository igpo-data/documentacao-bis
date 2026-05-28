import streamlit as st
import pandas as pd
import streamlit.components.v1 as components


def render():
    st.title("Análise Churn")

    st.info("""
    Objetivo desse BI é fazer uma ánalise do cliente com base no histórico de faturamento do pagador (CNPJ Principal). 

    """)

    abas = st.tabs([
        "Análise Churn ",
        "Detalhamento "
    ])

    with abas[0]:
    
        st.image(
                "img/Analise Churn.JPG",
                    caption="Tela da Analise Churn",
                    use_container_width=True
                     )


        st.markdown("""
                    <h5> Regra de Negócio – Classificação de Status do Cliente</h5>""", unsafe_allow_html=True)

        st.markdown("""    
            A classificação de status do cliente é realizada com base no histórico mensal de faturamento do pagador (CNPJ Principal), 
            considerando o mês mais recente disponível na base de dados como referência.


            **Clientes Carteira**: Total de clientes. 

            **Ativos**: Cliente que realizou frete no mês atual e mantém recorrência normal de fretes.
                Condição:  Faturou no mês atual e não se enquadra como Novo ou Reconquistado. 

            **Em risco**: São clientes que param há 1 a 3 meses, ou seja, clientes que não realizaram frete no mês atual e seu último frete ocorreu há no máximo 3 meses. 

            **Reconquista**: Cliente que voltou a faturar no mês atual após permanecer mais de 6 meses sem fretes. 
                Condição: Faturou no mês atual, possui histórico anterior e ficou mais de 6 meses sem faturar antes do retorno. 


            **Inativos**: Cliente que está há mais de 12 meses sem realizar fretes.

            **Observações Importantes**\n
            •	A análise é feita por CNPJ Principal do cliente.\n
            •	A referência de “mês atual” corresponde ao mês mais recente existente na base de dados.\n
            •	A classificação considera apenas clientes que possuem histórico de faturamento.\n
            •	O cliente pode mudar de status mensalmente conforme seu comportamento de frete.\n
                     """)
        

        ############################# Detalhamento ###############################
        st.markdown("""
                    <h4>Modelagem de Dados</h4>""", unsafe_allow_html=True)
        st.markdown("""Essa base ela advém da base 455.""")
        components.html("""
<div style="width:100%; overflow-x:auto;">
<div class="mermaid">

flowchart LR

    A["<b>fato_ClassificacaoCliente</b><br/><br/>
    id_GrupoPagador<br/>
    id_PeriodoAutorizacao<br/>
    kgs_PesoCalculadoKG<br/>
    nom_AgregacaoCliente<br/>
    nom_ClassificacaoCliente<br/>
    qtd_Cliente<br/>
    qtd_CTRC<br/>
    qtd_QuantidadeVolume<br/>
    vlr_ValorFrete<br/>
    vlr_ValorMercadoria"]

    B["<b>fato_EvolucaoCliente</b><br/><br/>
    id_GrupoPagador<br/>
    id_PeriodoAutorizacao<br/>
    id_UnidadeBeneficiaria<br/>
    dat_DataAutorizacao<br/>
    nom_StatusCliente<br/>
    qtd_Cliente<br/>
    vlr_FaturamentoMesAnterior<br/>
    vlr_FaturamentoMesAtual"]

    C["<b>fato_FreteExpedidoRecebido (455)</b><br/><br/>
    id_CTRC<br/>
    id_Destinatario<br/>
    id_Expedidor<br/>
    id_GrupoPagador<br/>
    id_Mercadoria<br/>
    id_Ocorrencia<br/>
    id_Pagador<br/>
    id_PeriodoAutorizacao<br/>
    id_PeriodoEmissao<br/>
    id_PeriodoMeta<br/>
    id_PeriodoPrevisaoEntrega"]

    D["<b>dim_GrupoClientePagador</b><br/><br/>
    id_GrupoPagador<br/>
    id_PeriodoUltimaCompra<br/>
    data_UltimaCompra<br/>
    nom_NomeGrupo<br/>
    nom_StatusCliente<br/>
    num_CNPJPrincipal"]

    E["<b>dim_PeriodoUltimaCompra</b><br/><br/>
    id_Periodo<br/>
    Data<br/>
    flg_DiaUtil<br/>
    flg_FeriadoNacional<br/>
    nom_Bimestre<br/>
    nom_BimestreAno<br/>
    nom_DiaSemana"]

    A -->|id_GrupoPagador| D
    B -->|id_GrupoPagador| D
    C -->|GrupoPagador| D

    D -->|id_PeriodoUltimaCompra| E

    style A fill:#fff4e6,stroke:#ff8c00,stroke-width:2px,color:#000
    style B fill:#fff4e6,stroke:#ff8c00,stroke-width:2px,color:#000
    style C fill:#fff4e6,stroke:#ff8c00,stroke-width:2px,color:#000

    style D fill:#e6f7ff,stroke:#1890ff,stroke-width:2px,color:#000
    style E fill:#e6f7ff,stroke:#1890ff,stroke-width:2px,color:#000

</div>
</div>

<script type="module">
import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';

mermaid.initialize({
    startOnLoad: true,
    theme: "dark",
    flowchart: {
        nodeSpacing: 120,
        rankSpacing: 150,
        curve: "basis"
    },
    themeVariables: {
        fontSize: "14px"
    }
});
</script>
""", height=850, scrolling=True)

    with abas[1]:
        st.header("Detalhamento")

       
