import streamlit as st
import pandas as pd
import streamlit.components.v1 as components


def render():
    st.title("Cotação")

    st.info("""
    Aqui coloca qual o objeto do BI 
    """)

    abas = st.tabs([
        "Cotação",
        "Cotação Origem Destino",
        "Ranking por Cotação",
        "Detalhamento",
        "Visão Comercial"
    ])

    with abas[0]:
    
    
        components.html("""
                    <div class="mermaid">
                    erDiagram

                        SSW_OP002 {
                            numeric COTACAO pk ,
                            text UNIDADE INCLUSAO,
                            text USUARIO INCLUSAO,
                            numeric CNPJ PAGADOR,
                            text NOME PAGADOR,
                            text ABC ,
                            text VENDEDOR,
                            text ORIGEM,
                            character varying(4) PRACA COLETA,
                            character varying(4) PRACA COMERCIAL,
                            text DESTINO,
                            numeric CNPJ DESTINATARIO,
                            text NOME DESTINATARIO,
                            text ED,
                            "TIPO FRETE" character varying(3) NULL,
                            "MERCADORIA" numeric NULL,
                            "VALOR NF" numeric NULL,
                            "QTD VOLUMES" numeric NULL,
                            "QTD PARES" numeric NULL,
                            "PESO" numeric NULL,
                            "CUBAGEM" numeric NULL,
                            "PESO CALCULO" numeric NULL,
                            "FRETE NTC" numeric NULL,
                            "PROPOSTA INICIAL" numeric NULL,
                            "PROPOSTA ATUAL" numeric NULL,
                            "DESC NTC" numeric NULL,
                            "RC" numeric NULL,
                            "DESC INICIAL" numeric NULL,
                            "TABELA DE CALCULO" text NULL,
                            "DATA HORA INCLUSAO" timestamp without time zone NULL,
                            "VALIDADE" timestamp without time zone NULL,
                            "SITUACAO" text NULL,
                            "CTRC" text NULL,
                            "DATA EMISSAO CTRC" timestamp without time zone NULL,
                            "FRETE CTRC" numeric NULL,
                            "RELATORIO COMISSAO" numeric NULL,
                            "UNIDADE RESPONSAVEL" text NULL,
                            "USUARIO ALTERACAO" text NULL,
                            "Data Atualização" timestamp without time zone NULL,
                            "CONTATO" text NULL,
                            "AUTORIZADO" text NULL


                        }

                        DIM_002 {
                            int id_op002 PK
                            bigint COTACAO FK
                            text ORIGEM
                            text DESTINO
                            text TIPO_FRETE
                            text MERCADORIA
                            text SITUACAO
                            text CTRC
                            text USUARIO_INCLUSAO
                            text VENDEDOR
                        }

                        FT_002 {
                            int sk_op002 FK
                            int sk_dt_inclusao FK
                            int sk_validade FK
                            int sk_dt_emis_ctrc FK
                            int sk_cnpj_pagador FK
                            int sk_cnpj_dest FK
                            numeric vlr_mercadoria
                            numeric vlr_nfe
                            numeric peso
                            numeric peso_calculo
                            numeric vlr_proposta_inicial
                            numeric vlr_proposta_atual
                            numeric vlr_emitida
                            numeric vlr_perdido
                            numeric desconto
                        }

                        DIM_TEMPO {
                            int id_dim_tempo PK
                            date data
                            int ano
                            int mes
                            text nome_mes
                            int Alt_Dia_Util
                            text feriado
                        }

                        DIM_CLIENTE {
                            int sk_dim_cliente PK
                            text cnpj
                            text cnpj_principal
                            text nome_cliente
                        }

                        VW_DIM_FATO_002 {
                            int id_op002
                            bigint COTACAO
                            text ORIGEM
                            text DESTINO
                            text SITUACAO
                            text CTRC
                            numeric vlr_proposta_inicial
                            numeric vlr_proposta_atual
                            numeric vlr_emitida
                            date dt_inclusao
                            date dt_validade
                            date dt_emissao_ctrc
                            text cnpj_pagador
                            text cliente_pagador
                            text cnpj_destinatario
                            text cliente_destinatario
                        }

                        SSW_OP002 ||--|| DIM_002 : "COTACAO = COTACAO"
                        DIM_002 ||--|| FT_002 : "id_op002 = sk_op002"
                        FT_002 }o--|| DIM_TEMPO : "sk_dt_inclusao = id_dim_tempo"
                        FT_002 }o--|| DIM_TEMPO : "sk_validade = id_dim_tempo"
                        FT_002 }o--|| DIM_TEMPO : "sk_dt_emis_ctrc = id_dim_tempo"
                        FT_002 }o--|| DIM_CLIENTE : "sk_cnpj_pagador = sk_dim_cliente"
                        FT_002 }o--|| DIM_CLIENTE : "sk_cnpj_dest = sk_dim_cliente"

                        DIM_002 ||--|| VW_DIM_FATO_002 : "base da view"
                        FT_002 ||--|| VW_DIM_FATO_002 : "métricas da view"
                        DIM_TEMPO ||--|| VW_DIM_FATO_002 : "datas"
                        DIM_CLIENTE ||--|| VW_DIM_FATO_002 : "clientes"

                    </div>

                    <script type="module">
                    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
                    mermaid.initialize({ startOnLoad: true });
                    </script>
                    """, height=2500)
      



      
########------------Visão Geral ------------------########
        with abas[1]:
            st.markdown("""
                        <h4>Visual:</h4>""", unsafe_allow_html=True)
            
            ##### Depois adiciona  diagrama #####
            ##components.html("""
                ##<div class="mermaid">
                    ##erDiagram

                    
                        

                        ##dim_PeriodoMetaDiaria ||--o{ fato_MetaUnidadeDiaria : Periodo_Meta
                        ##dim_UnidadeBeneficiaria ||--o{ fato_MetaUnidadeDiaria : Unidade

                        ##dim_PeriodoAutorizacao ||--o{ fato_FreteExpedidoRecebido : PeriodoAut
                        ##dim_PeriodoEmissao ||--o{ fato_FreteExpedidoRecebido : PeriodoEmissao
                        ##dim_UnidadeBeneficiaria ||--o{ fato_FreteExpedidoRecebido : Unidade

                    ##</div>

                    ##<script type="module">
                    ##import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
                    ##mermaid.initialize({ startOnLoad: true });
                    ##</script>
                    ##""", height=800)

            st.markdown("""Neste BI se encontra a quantidade de dias úteis dentro daquele Mês, dessa forma, o 
                        mês de abril há 21 dias úteis tirando os feriados e contabilizando o sabado como 0,25 para fins 
                        de faturamento. 
            """ )

            st.image(
                    "img/Comercial_Geral_Visão_Geral_PF.PNG",
                        caption="Tabela de exportação.",
                        use_container_width=True
                        )

            st.table({
                "Fonte": ["tabela_exemplo"],
                "Tipo": ["Tabela PostgreSQL"],
                "Descrição": ["Descrever o uso dessa tabela"]
            })

            st.markdown("""
                        <h4>Modelagem de Dados</h4>""", unsafe_allow_html=True)

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
