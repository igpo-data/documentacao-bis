import streamlit as st
import pandas as pd
import streamlit.components.v1 as components


def render():
    st.title("Anomalias e Cancelamento")

    st.info("""
    Painel com objetivo de mostrar os CTRC's que tiveram solicitação
    de alteração e que foram cancelados nas respectivas telas. 
    """)

    abas = st.tabs([
        "Anomalias",
        "Cancelamento"        
    ])

    with abas[0]:
        ##st.header("Titulo Grandão")

        st.markdown("""
                    <h5>Filtros:</h5>""", unsafe_allow_html=True)

        st.markdown("""
      *dim_PeriodoAutorizacao:* Período advindo da 455.
      *dim_UnidadeBeneficiaria:* Unidade de Origem do CTRC, ou seja os três primeiros digitos do CTRC. 
      *fato_RequisicaoDesconto (nom_status):* Status advindos da extensão. 
      *fato_RequisicaoDesconto (nom_Tipo):* Coluna importante pro encaminhamento do processo da solicitação. 
      *fato_RequisicaoDesconto (nom_Razao):* Motivo principal de alteração, advém de um menu suspenso dentro da extensão.
      *fato_RequisicaoDesconto (nom_SiglaCTRC):* Coluna que advém da fato sendo restrita a extensão, diferente da dim_CTRC que advém da 455. 
                    \n 
                   """)
    
    
      

   