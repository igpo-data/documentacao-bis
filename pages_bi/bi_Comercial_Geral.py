# pages_bi/modelo_bi.py
import streamlit as st
import pandas as pd
import streamlit.components.v1 as components


def render():
    st.title("Comercial Geral")

    st.info("""
    
    """)

    abas = st.tabs([
        "Acompanhamento Diária",
        "Visão Geral",
        "Visão Diária",
        "Resumo de Faturamento",
        "Resumo de Vendas",
        "Carteira de Vendedores",
        "Carteira de Vendedores - Detalhada",
        "Indicador LTV",
        "Origem Frete",
        "Farol de Metas",
        "Análise de Unidades", 
        "Análise de Clientes",
        "Fat x Metas",
        "Wallet Share",
        "Avaliações",
        "Expansão Estratégica",
        "SLA Next IP",
        "Histograma de Dias Entrega"
    ])

    with abas[0]:
        #st.header("Titulo Grandão")

        st.markdown("""
                    <h4>Visual:</h4>""", unsafe_allow_html=True)

        st.image(
        "img/Acomp_Geral_Principal.PNG",
        caption="Tela principal do BI",
        use_container_width=True
        )
        
        st.markdown("""
       Nele há o filtro por *dim_PeriodoMetaDiaria*  como um período dinâmico e outro período que 
    consta na mesma tabela, dois filtros por questão de preferência de usuário. 
    \n 
     O filtro dessa tela obrigatoriamente há de ser pela *dim_UnidadeBeneficiaria* e
    dentro do filtro eu tenho o conjunto de *nom_RegiaoCentro*: E-commerce, Embarcadora,
    Filial, Inativo, Meio Norte , Ms Norte, Ms Sul, MTZ, Norte, Oeste , Pará, 
    Parceira, Redespacho, Rodotech, Rondonia, Sul, Sul- Pará e Vale.  """)
        
        #--------DEIXA AQUI QUANDO EU PRECISA::::::::
        #col1, col2, col3 = st.columns(3)
        #col1.metric("Indicador 1", "0")
        #col2.metric("Indicador 2", "0%")
        #col3.metric("Indicador 3", "R$ 0,00")

        st.image(
                "img/Filtros.PNG",
                    caption="Banner BI Comercial",
                    use_container_width=True
                     )
        
        st.markdown("""
            Nela há **Quantidades de CT-e** advindo obrigatoriamente da 455, 
            dentro deles temos os rótulos de referência: <span style="background-color:#FFF3B0; padding:2px 6px; border-radius:5px;">
            Quantidade CT-e Dia Anterior Meta Diaria
            </span>, <span style="background-color:#FFF3B0; padding:2px 6px; border-radius:5px;">
            Quantidade CT-e Dia Atual Meta Diaria
            </span>,<span style="background-color:#FFF3B0; padding:2px 6px; border-radius:5px;">
            Quantidade CT-e LM Meta Diaria</span>. Sendo LM como a quantidade no mês passado.
            """, unsafe_allow_html=True)
        
        st.markdown("""
           A mesma análise acontece com o **Faturamento realizado** (Valor Frete Bruto) 
        dentro daquele período filtrado, a medida corresponde à soma do Valor do Frete Bruto advindo da opção 455. 
        Há adjunto também os rótulos de referência: 
        <span style="background-color:#FFF3B0; padding:2px 6px; border-radius:5px;">
         Valor Frete Bruto Dia Anterior Meta Diaria
        </span>, <span style="background-color:#FFF3B0; padding:2px 6px; border-radius:5px;"> Valor Frete Bruto Dia Atual Meta Diaria
        </span>, <span style="background-color:#FFF3B0; padding:2px 6px; border-radius:5px;">
        Valor Frete Bruto LM Meta Diaria</span>""", unsafe_allow_html=True)
        
        st.markdown("""
           A **Meta de Faturamento** (Valor Meta Unidade Diaria) advém de uma planilha externa e 
        imputada dentro do modelo semântico. Há adjunto também os rótulos de referência: 
        <span style="background-color:#FFF3B0; padding:2px 6px; border-radius:5px;">
        Valor Faltante Meta Diaria
        </span>, <span style="background-color:#FFF3B0; padding:2px 6px; border-radius:5px;">
        Valor Frete Projetado Meta Diaria
        </span>. Sendo o primeiro a diferença entre a meta e o Valor Frete Bruto e o 
        segundo quanto você já faturou até agora ÷ quantos dias úteis já passaram × total de dias úteis do mês.
        """, unsafe_allow_html=True)

        st.image(
                "img/Table_Acomp_Diario.PNG",
                    caption="Tabela de exportação.",
                    use_container_width=True
                     )
        
        st.markdown("""
           A **Meta de Faturamento** (Valor Meta Unidade Diaria) advém de uma planilha externa e 
        imputada dentro do modelo semântico. Há adjunto também os rótulos de referência: 
        <span style="background-color:#FFF3B0; padding:2px 6px; border-radius:5px;">
        Valor Faltante Meta Diaria
        </span>, <span style="background-color:#FFF3B0; padding:2px 6px; border-radius:5px;">
        Valor Frete Projetado Meta Diaria
        </span>. Sendo o primeiro a diferença entre a meta e o Valor Frete Bruto e o 
        segundo quanto você já faturou até agora ÷ quantos dias úteis já passaram × total de dias úteis do mês.
        """, unsafe_allow_html=True)

       
        tabela = pd.DataFrame({

                    "Coluna": [
                    "Data",
                    "Qtde CT-e",
                    "Faturamento",
                    "Meta Faturamento",
                    "% Meta Atingida Diaria",
                    "Peso",
                    "Meta Peso",
                    "% Meta Peso Atingido",
                    "Média KG",
                    "Meta Média KG",
                    "% Meta KG Atingida",
                    "Ticket Médio",
                    "Dia Semana"
                ],

                "O que significa": [
                    "dim_PeriodoMetaDiaria",
                    "Quantidade de CT-es emitidos",
                    "Valor total faturado bruto no dia",
                    "Valor esperado de faturamento para o dia",
                    "Percentual atingido da meta diária",
                    "Peso total transportado",
                    "Meta de peso diário",
                    "Percentual da meta de peso",
                    "Receita média por KG",
                    "Meta esperada por KG",
                    "Percentual da meta KG",
                    "Valor médio por CT-e",
                    "Dia da semana da operação"
                ],

                "Origem/Relação": [
                    "dim_PeriodoMetaDiaria",
                    "SSW 455",
                    "SSW 455",
                    "Planilha SharePoint",
                    "Medida da 455",
                    "Medida da 455",
                    "Planilha SharePoint",
                    "455 + SharePoint",
                    "Medida da 455",
                    "455 + SharePoint",
                    "455 + SharePoint",
                    "Medida da 455",
                    "dim_PeriodoMetaDiaria"]})

        st.dataframe(
                    tabela,
                    use_container_width=True,
                    hide_index=True
                )
        st.image(
                "img/Indi_Acomp_Diario.PNG",
                    caption="Indicadores Pontuais",
                    use_container_width=True
                     )
        st.markdown("""
           O **Realizado**  é o faturamento realizado dividido Meta de Faturamento e mostrado em formato de porcentagem. 
                    \n 
        O **Projetado** é o Frete Projetado dividido pela Meta de Faturamento. Sendo o Frete Projetado o valor do Faturamento Atual 
        dividido pelos dias úteis corridos vezes dias úteis totais. Analisando de fato esse indicador responde à pergunta:
        “Se a operação continuar performando como está hoje, quanto da meta mensal será alcançado?” 
                            \n
        O **Faturamento** por Tipo de Frete é subdivido entre dois tipo: CIF + TER e FOB. 
        O primeiro representa o valor total de frete das operações em que o pagamento do transporte é responsabilidade do remetente 
        da mercadoria ou algum terceiro, já o segundo é o valor do frete das operações em que o destinatário/cliente é quem paga o transporte. 
        Dentro disso, há metas, realizado e sua porcentagem do quanto que se alcançou. 
        \n 
        Um ponto importante que o filtro de unidade está em relação a Unidade que se Beneficia deste frete. """)

        st.markdown("""
                    <h4>Modelagem de Dados</h4>""", unsafe_allow_html=True)
    
        components.html("""
                            <div style="width:100%; overflow-x:auto;">
                            <div class="mermaid">
                            flowchart LR

                                A["dim_PeriodoMetaDiaria<br/>
                                Data<br/>
                                flg_DiaUtil<br/>
                                num_Ano<br/>
                                nom_Mes<br/>
                                num_Dia"]

                                B["fato_MetaUnidadeDiaria<br/>
                                pct_Meta_Atingida<br/>
                                pct_Meta_KG<br/>
                                pct_Meta_Peso<br/>
                                vlr_Meta_Media_KG<br/>
                                vlr_Meta_Peso_KG<br/>
                                vlr_Meta_Unidade"]

                                C["dim_UnidadeBeneficiaria<br/>
                                cod_Unidade<br/>
                                nom_RegiaoCentro<br/>
                                nom_VinculoCentro"]

                                D["dim_PeriodoAutorizacao<br/>
                                Data<br/>
                                flg_DiaUtil<br/>
                                flg_FeriadoNacional"]

                                E["dim_PeriodoEmissao<br/>
                                nom_Bimestre<br/>
                                nom_BimestreAno<br/>
                                nom_DiaSemana"]

                                F["fato_FreteExpedidoRecebido<br/>
                                qtd_CTe<br/>
                                vlr_Frete_Bruto<br/>
                                vlr_Frete_por_CTe<br/>
                                vlr_Frete_por_Peso"]

                                A -->|Periodo_Meta| B
                                C -->|Unidade_Meta| B
                                C -->|Unidade_Frete| F
                                D -->|id_Periodo| F
                                E -->|id_PeriodoEmissao| F

                                style A fill:#f7f4ff,stroke:#7b61ff,stroke-width:1px
                                style B fill:#fff8e8,stroke:#d69e2e,stroke-width:1px
                                style C fill:#f7f4ff,stroke:#7b61ff,stroke-width:1px
                                style D fill:#f7f4ff,stroke:#7b61ff,stroke-width:1px
                                style E fill:#f7f4ff,stroke:#7b61ff,stroke-width:1px
                                style F fill:#fff8e8,stroke:#d69e2e,stroke-width:1px

                            </div>
                            </div>

                            <script type="module">
                            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';

                            mermaid.initialize({
                                startOnLoad: true,
                                theme: "default",
                                flowchart: {
                                    nodeSpacing: 90,
                                    rankSpacing: 120,
                                    curve: "basis"
                                },
                                themeVariables: {
                                    fontSize: "13px"
                                }
                            });
                            </script>
                            """, height=750, scrolling=True)

        
########------------Visão Geral ------------------########
    with abas[1]:
                st.markdown("""
                            <h5>Projeção Filial:</h5>""", unsafe_allow_html=True)

                st.markdown("""Neste BI se encontra a quantidade de dias úteis dentro daquele mês, por exemplo, o 
                            mês de abril de 2026 há 21 dias úteis tirando os feriados e contabilizando o sábado como 0,25 para fins 
                            de faturamento. 
                """ )
                st.markdown("""Outro ponto, o **Realizado**  Valor Frete advindo da 455, tirando as ocorrências 87 e 83 e o
                             tipo de baixa CANCELADO e LIQU OCOR. 
                """ )
                st.image(
                        "img/Comercial_Geral_Visão_Geral_PF_FiltroOco.PNG",
                            caption="dim_Ocorrencia",
                            use_container_width=True
                            )
                
                st.markdown("""Observação na modelagem do painel há obrigatoriedade da dim_Ocorrência 
                            já esteja modelada com seguintes colunas: 
                """ )

                st.table({
                       "Coluna": [
                            "cod_Ativo",
                            "cod_Ocorrencia",
                            "cod_Processo",
                            "cod_Tipo",
                            "id_Ocorrencia",
                            "nom_Empresa",
                            "nom_Ocorrencia"
                        ],

                        "O que significa": [
                            "Identifica se a ocorrência está ativa",
                            "Código da ocorrência",
                            "Código do processo relacionado",
                            "Código do tipo da ocorrência",
                            "Identificador único da ocorrência",
                            "Nome do dominio que advém do SSW",
                            "Nome/descrição da ocorrência"
                        ],
                })

                        

                
                st.markdown("""Tabela de Exportação da Projeção Filial:      """ )

                ##completar 
                st.markdown("""
                            <h5>Modelagem de Dados</h5>""", unsafe_allow_html=True)
                ##completar 
                st.markdown("""Tela de Crescimento:
                 \\
                           
                             """)
                


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