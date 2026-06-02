import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from streamlit_image_coordinates import streamlit_image_coordinates
import base64
from pathlib import Path

st.set_option('client.showErrorDetails', True)

def render():
    st.title("Performance Geral")

    st.info(""" Performance Geral é um BI que tem como fontes de dados a base 455 (+ complementar B) e 36 do SSW. """)

    abas = st.tabs([
        "Performan Geral - Autorização",
        "Performance Unidade/Cliente - Autorização",
        "Performance Região",
        "Previsão de Entregas - Resumo",
        "Previsão de Entregas - Quadro Geral",
        "Previsão de Entregas - Emissão",
        "Previsão de Unidade/Cliente Emissão",
        "Efetividade de Entregas - Motoristas",
        "Efetividade de Entregas - Evolução",
        "Efetividade de Entregas - Retornados",
        "Efetividade de Entregas - Mensal",
        "Efetividade de Entregas Tipo de Operação e Torre",
        "Efetividade de Entrega - CTEs Romaneados",
        "Performance Prioridade CGB"
    ])

    with abas[0]:
        st.markdown("""
                    <h4>Filtros: </h4>""", unsafe_allow_html=True)
        
        st.markdown("""
      **Período de Autorização** - *dim_PeriodoAutorizacao*: Período que advém da 455.\n
      **Origem:** - *dim_UnidadeEmissora*: Utiliza aqui nom_UnidadeEmissora e nom_VinculoCentro.\n
      **Destino** - *dim_UnidadeReceptora*: Utiliza aqui cod_UnidadeReceptora e nom_VinculoCentro.\n
      **Ocorrência** - *dim_Ocorrencia*: cod_Ocorrência, a qual é constituída pela 455 complementar B. \n
      **Pagador** - *dim_Pagador*: utiliza nom_ClientePagador o qual advém da 455.\n
      **Status** - *fato_FreteExpedidoRecebido*: utiliza a nom_StatusEntregaPendente, o qual é um atributo dentro das tabelas
                    de medidas advindas da 455, as quais há análise dos CTRC com ocorrência 1 (entrega), dentro disso se avalia se foram dentro ou fora do prazo.\n
      **CTRC** - *dim_CTRC*: utiliza a coluna nom_SiglaCTRC, o qual é todos os CTRC’s da tabela 455 durante aquele período filtrado. """)
        
        st.markdown("""
                    <h5>Sistema de Paginação</h5>""", unsafe_allow_html=True)
        
        st.markdown("""Há uma dupla tela uma filtrada por Período de Autorização e outra filtrada por Período de Previsão de Entrega na visão geral""")
        
        col1, col2 = st.columns(2)

        with col1:
                st.image("img/Performance_Geral_Autorizacao.PNG", caption="Tela filtrada pelo período de Autorização", use_container_width=True)

        with col2:
            st.image("img/Performance_Geral_Previsao_Entrega.PNG", caption="Tela Filtrada pelo período de Previsão de Entrega ", use_container_width=True)
   
        ##st.image("img/Performance_Geral-pg.jpg", caption="Sistema de Botões do Painel", use_container_width=True)
    
##################Imagens dos cards #########################
        st.markdown("""Também há vários 17 cards que levam a outras páginas: """)

        
        def img_to_base64(path):
            img_bytes = Path(path).read_bytes() 
            return base64.b64encode(img_bytes).decode()

        def render_mapa_interativo():
            imagem_principal = img_to_base64("img/Performance_Geral-pg.jpg")

                        # Troque essas imagens pelas imagens de detalhe de cada card
            imagens = {
                                            "card_1": img_to_base64("img/Performance_Geral_Entregue.PNG"),
                                            "card_2": img_to_base64("img/Performance_Geral_Fora_Prazo_Cliente.PNG"),
                                            "card_3": img_to_base64("img/Performance_Geral_Fora_Prazo_Trans.PNG"),
                                            "card_4": img_to_base64("img/Performance_Geral_Previstos_Fora_Prazo.PNG"),
                                            "card_5": img_to_base64("img/Performance_Geral_Atrasados_3.PNG"),
                                            "card_6": img_to_base64("img/Performance_Geral_Atrasados_5.PNG"),
                                            "card_7": img_to_base64("img/Performance_Geral_Atrasados_8.PNG"),
                                            "card_8": img_to_base64("img/Performance_Geral_Atrasados_15.PNG"),
                                            "card_9": img_to_base64("img/Performance_Geral_Atrasados_30.PNG"),
                                            "card_10": img_to_base64("img/Performance_Geral_Atrasados_30+.PNG"),
                                            "card_11": img_to_base64("img/Performance_Geral_Previstos_Prazo.PNG"),
                                            "card_12": img_to_base64("img/Performance_Geral_Previstos_Hoje.PNG"),
                                            "card_13": img_to_base64("img/Performance_Geral_Previstos_d+1.PNG"),
                                            "card_14": img_to_base64("img/Performance_Geral_Previstos_d+2.PNG"),
                                            "card_15": img_to_base64("img/Performance_Geral_Previstos_d+3.PNG"),
                                            "card_16": img_to_base64("img/Performance_Geral_Previstos_d+4.PNG"),
                                            "card_17": img_to_base64("img/Performance_Geral_Previstos_d5+.PNG"),
                                            }
            html = f"""
                    <style>
                         .container {{
                                position: relative;
                                width: 100%;
                                max-width: 1280px;
                                margin: auto;
                            }}

                            .main-img {{
                                width: 100%;
                                border-radius: 10px;
                            }}

                            .hotspot {{
                                position: absolute;
                                cursor: pointer;
                                border: 2px solid transparent;
                                transition: 0.2s;
                            }}

                            .hotspot:hover {{
                                border: 3px solid red;
                                background: rgba(255, 0, 0, 0.12);
                                box-shadow: 0 0 12px rgba(255,0,0,0.7);
                            }}

                            .preview {{
                                display: none;
                                position: absolute;
                                width: 330px;
                                z-index: 50;
                                background: white;
                                padding: 6px;
                                border-radius: 12px;
                                box-shadow: 0 8px 28px rgba(0,0,0,0.35);
                                top: 105%;
                                left: 0;
                            }}

                            .hotspot:hover .preview {{
                                display: block;
                                animation: fadeIn 0.25s ease;
                            }}

                            .preview img {{
                                width: 100%;
                                border-radius: 8px;
                            }}

                            .modal {{
                                display: none;
                                position: fixed;
                                z-index: 9999;
                                left: 0;
                                top: 0;
                                width: 100%;
                                height: 100%;
                                background: rgba(0,0,0,0.78);
                                align-items: center;
                                justify-content: center;
                            }}

                            .modal-content {{
                                max-width: 85%;
                                max-height: 85%;
                                border-radius: 16px;
                                animation: zoomIn 0.35s ease;
                                box-shadow: 0 12px 40px rgba(0,0,0,0.6);
                            }}

                            .close {{
                                position: absolute;
                                top: 25px;
                                right: 45px;
                                color: white;
                                font-size: 42px;
                                font-weight: bold;
                                cursor: pointer;
                            }}

                            @keyframes zoomIn {{
                                from {{
                                    transform: scale(0.55);
                                    opacity: 0;
                                }}
                                to {{
                                    transform: scale(1);
                                    opacity: 1;
                                }}
                            }}

                            @keyframes fadeIn {{
                                from {{
                                    opacity: 0;
                                    transform: translateY(10px);
                                }}
                                to {{
                                    opacity: 1;
                                    transform: translateY(0);
                                }}
                            }}
                    </style>

                    <div class="container">
                            <img class="main-img" src="data:image/jpg;base64,{imagem_principal}">

                            <div class="hotspot" onclick="openModal('card_1')" style="left:16.4%; top:20.3%; width:15.6%; height:14.3%;">
                                <div class="preview"><img src="data:image/png;base64,{imagens["card_1"]}"></div>
                            </div>

                            <div class="hotspot" onclick="openModal('card_2')" style="left:58.3%; top:23.1%; width:5.2%; height:5.3%;">
                                <div class="preview"><img src="data:image/png;base64,{imagens["card_2"]}"></div>
                            </div>

                            <div class="hotspot" onclick="openModal('card_3')" style="left:58.3%; top:28.7%; width:5.2%; height:5.3%;">
                                <div class="preview"><img src="data:image/png;base64,{imagens["card_3"]}"></div>
                            </div>

                            <div class="hotspot" onclick="openModal('card_4')" style="left:1.2%; top:39%; width:16.5%; height:29%;">
                                <div class="preview"><img src="data:image/png;base64,{imagens["card_4"]}"></div>
                            </div>

                            <div class="hotspot" onclick="openModal('card_5')" style="left:18.2%; top:39%; width:10%; height:14.5%;">
                                <div class="preview"><img src="data:image/png;base64,{imagens["card_5"]}"></div>
                            </div>

                            <div class="hotspot" onclick="openModal('card_6')" style="left:18.2%; top:54.2%; width:10%; height:13.7%;">
                                <div class="preview"><img src="data:image/png;base64,{imagens["card_6"]}"></div>
                            </div>

                            <div class="hotspot" onclick="openModal('card_7')" style="left:28.7%; top:39%; width:10%; height:14.5%;">
                                <div class="preview"><img src="data:image/png;base64,{imagens["card_7"]}"></div>
                            </div>

                            <div class="hotspot" onclick="openModal('card_8')" style="left:28.7%; top:54.2%; width:10%; height:13.7%;">
                                <div class="preview"><img src="data:image/png;base64,{imagens["card_8"]}"></div>
                            </div>

                            <div class="hotspot" onclick="openModal('card_9')" style="left:39.2%; top:39%; width:10%; height:14.5%;">
                                <div class="preview"><img src="data:image/png;base64,{imagens["card_9"]}"></div>
                            </div>

                            <div class="hotspot" onclick="openModal('card_10')" style="left:39.2%; top:54.2%; width:10%; height:13.7%;">
                                <div class="preview"><img src="data:image/png;base64,{imagens["card_10"]}"></div>
                            </div>

                            <div class="hotspot" onclick="openModal('card_11')" style="left:51.3%; top:39%; width:16%; height:29%;">
                                <div class="preview"><img src="data:image/png;base64,{imagens["card_11"]}"></div>
                            </div>

                            <div class="hotspot" onclick="openModal('card_12')" style="left:68.2%; top:39%; width:9.9%; height:13.7%;">
                                <div class="preview"><img src="data:image/png;base64,{imagens["card_12"]}"></div>
                            </div>

                            <div class="hotspot" onclick="openModal('card_13')" style="left:68.2%; top:54.2%; width:9.9%; height:13.7%;">
                                <div class="preview"><img src="data:image/png;base64,{imagens["card_13"]}"></div>
                            </div>

                            <div class="hotspot" onclick="openModal('card_14')" style="left:78.6%; top:39%; width:9.9%; height:13.7%;">
                                <div class="preview"><img src="data:image/png;base64,{imagens["card_14"]}"></div>
                            </div>

                            <div class="hotspot" onclick="openModal('card_15')" style="left:78.6%; top:54.2%; width:9.9%; height:13.7%;">
                                <div class="preview"><img src="data:image/png;base64,{imagens["card_15"]}"></div>
                            </div>

                            <div class="hotspot" onclick="openModal('card_16')" style="left:89.1%; top:39%; width:9.7%; height:13.7%;">
                                <div class="preview"><img src="data:image/png;base64,{imagens["card_16"]}"></div>
                            </div>

                            <div class="hotspot" onclick="openModal('card_17')" style="left:89.1%; top:54.2%; width:9.7%; height:13.7%;">
                                <div class="preview"><img src="data:image/png;base64,{imagens["card_17"]}"></div>
                            </div>
                    </div>

                    <div id="modal" class="modal" onclick="closeModal()">
                            <span class="close">&times;</span>
                            <img id="modal-img" class="modal-content">
                    </div>

                    <script>
                            const imagens = {{
                                card_1: "data:image/png;base64,{imagens["card_1"]}",
                                card_2: "data:image/png;base64,{imagens["card_2"]}",
                                card_3: "data:image/png;base64,{imagens["card_3"]}",
                                card_4: "data:image/png;base64,{imagens["card_4"]}",
                                card_5: "data:image/png;base64,{imagens["card_5"]}",
                                card_6: "data:image/png;base64,{imagens["card_6"]}",
                                card_7: "data:image/png;base64,{imagens["card_7"]}",
                                card_8: "data:image/png;base64,{imagens["card_8"]}",
                                card_9: "data:image/png;base64,{imagens["card_9"]}",
                                card_10: "data:image/png;base64,{imagens["card_10"]}",
                                card_11: "data:image/png;base64,{imagens["card_11"]}",
                                card_12: "data:image/png;base64,{imagens["card_12"]}",
                                card_13: "data:image/png;base64,{imagens["card_13"]}",
                                card_14: "data:image/png;base64,{imagens["card_14"]}",
                                card_15: "data:image/png;base64,{imagens["card_15"]}",
                                card_16: "data:image/png;base64,{imagens["card_16"]}",
                                card_17: "data:image/png;base64,{imagens["card_17"]}"
                            }};

                            function openModal(card) {{
                                document.getElementById("modal-img").src = imagens[card];
                                document.getElementById("modal").style.display = "flex";
                            }}

                            function closeModal() {{
                                document.getElementById("modal").style.display = "none";
                            }}
                    </script>
                        """

            components.html(html, height=750, scrolling=False)
        render_mapa_interativo()
    
        dados_cards = [
                                ["1", "Entregue"],
                                ["2", "Cliente"],
                                ["3", "Transportadora"],
                                ["4", "Previstos Fora do Prazo"],
                                ["5", "Previstos Atrasados em até 03 Dias"],
                                ["6", "Previstos Atrasados em até 15 Dias"],
                                ["7", "Previstos Atrasados em até 05 Dias"],
                                ["8", "Previstos Atrasados em até 30 Dias"],
                                ["9", "Previstos Atrasados em até 08 Dias"],
                                ["10", "Previstos Atrasados Acima de 30 Dias"],
                                ["11", "Previstos No Prazo"],
                                ["12", "Previstos para Hoje"],
                                ["13", "PrevistosD + 3"],
                                ["14", "Previstos D + 1"],
                                ["15", "Previstos D + 4"],
                                ["16", "Previstos D + 2"],
                                ["17", "Previstos Acima 5 Dias."],
                            ]

        tabela = pd.DataFrame(
                                dados_cards,
                                columns=["Card", "Indicador"]
                            )

        col1, col2 = st.columns([1, 2])

        with col1:
                                    st.subheader("📋 Cards")
                                    st.table(
                                        tabela.style.hide(axis="index")
                                    )

        with col2:
                                    #st.subheader("📝 Descrição")

                                    st.markdown("""
                                #### Hierarquia e Interpretação das Métricas de Entrega de CT-e

                        As métricas de acompanhamento da operação foram estruturadas de forma hierárquica,
                        permitindo que o usuário compreenda o comportamento das entregas distribuidas por ocorrência e 
                        por Unidade de Destino. A base de toda a análise é a **Quantidade Total de CT-es**, que representa 
                        todos os conhecimentos de transporte considerados no período selecionado.

                        A partir desse total, os CT-es são divididos em dois grandes grupos: **Entregues** e **Pendentes**. 
                        Os CT-es entregues correspondem aos CT-e com última ocorrencia 1, enquanto os CT-es pendentes 
                        representam as CT-e com as demais ocorrências e que ainda se encontram em trânsito ou 
                        aguardando conclusão da entrega.

                        Dentro do grupo de CT-es entregues, existe uma nova subdivisão entre **Entregues no Prazo** e 
                        **Entregues Fora do Prazo**. Essa classificação permite avaliar o nível de cumprimento do SLA operacional 
                        da empresa. Os CT-es entregues fora do prazo são detalhados em duas categorias: 
                        **Fora do Prazo por Responsabilidade do Cliente** e **Fora do Prazo por Responsabilidade da Transportadora**. 

                        Já os CT-es pendentes são classificados em **Pendentes no Prazo** e **Pendentes Fora do Prazo**. 
                        Os pendentes no prazo representam as entregas que ainda possuem tempo disponível para
                        serem concluídas dentro do SLA estabelecido. Para facilitar a gestão operacional e a
                        priorização das entregas, esses registros são distribuídos em faixas de previsão, como 
                        **Hoje (D0)**, **D+1**, **D+2**, **D+3**, **D+4** e **Acima de 5 Dias**. 
                        Essas faixas indicam quantos dias faltam para o vencimento da previsão de entrega e 
                        permitem à operação atuar preventivamente sobre cargas que estão se aproximando da data limite.

                        Por outro lado, os CT-es pendentes fora do prazo representam entregas cujo prazo previsto já foi ultrapassado. 
                        Esses registros também podem ser classificados em faixas de atraso, como **Até 3 Dias**, 
                        **Até 5 Dias**, **Até 8 Dias**, **Até 15 Dias**, **Até 30 Dias** e **Acima de 30 Dias**. 
                        Essa segmentação permite identificar o envelhecimento de pendências, facilitando
                        a priorização das entregas mais críticas e a atuação sobre ocorrências que podem impactar 
                        diretamente a satisfação do cliente e os indicadores de qualidade.

                        O **SLA de Entrega** mede a proporção de CT-es entregues em relação ao total de CT-es analisados,
                        demonstrando o percentual de cargas já concluídas. Já o **SLA de Entrega no Prazo** considera apenas os 
                        CT-es entregues dentro do prazo e os compara com o volume total de CT-es, fornecendo uma visão direta da 
                        eficiência operacional no cumprimento dos compromissos assumidos com os clientes.
                        Ainda é importante lembrar que o card 2 é sobre CTRC em que há ocorrências do tipo CLIENTE (03, 05, 06, 07, 08, 09, 10
                        11, 14, 22, 23, 29, 32, 38, 41, 46, 49, 50, 58, 64, 65, 66, 71, 74, 80, 84 e 92.)
                                """)
        st.image("img/Diagrama.png", caption="Diagrama das principais medidas de Perfomance geral.", width=450)

            
    ########------------Performance Unidade/Cliente-Autorização ------------------########
    with abas[1]:
            st.markdown("""
                        <h5>Tela Inicial :</h5>""", unsafe_allow_html=True)
            st.markdown(""" Dentro desse BI's há também dois filtros, por parte da data de autorização do CTRC e 
                        por parte da data de previsão de entrega. 
            """ )

            st.markdown(""" De maneira geral, esse BI é feito de *dim* que estão dentro da 455, sendo elas: 
            dim_UnidadeEmissora (nom_UnidadeEmissora),
            dim_UnidadeReceptora(nom_UnidadeReceptora), 
            dim_CTRC (nom_siglaCTRC),
            dim_Ocorrência (cod_Ocorrência e cod_Tipo),
            dim_PeriodoEmissão (Data),
            fato_FreteExpedidoRecebido (dat_DataPrevisãoEntrega),
            fato_FreteExpedidoRecebido (dat_DataEntregaRealizada),
            dim_Pagador (nom_ClientePagador),
            dim_TipoDocumento (nom_TipoDocumento),
            fato_FreteExpedidoRecebido (nom_StatusEntrega),
            quantidade de CT-e entregues .

            """ )

            col1, col2 = st.columns(2)

            with col1:
                        st.image("img/Performance_Unidade _Autorizacao.png", caption="Tela filtrada pelo período de Autorização", use_container_width=True)

            with col2:
                    st.image("img/Performance_Unidade_Previsao.png", caption="Tela Filtrada pelo período de Previsão de Entrega ", use_container_width=True)
                    
            

            st.markdown("""Nesta tela são realizadas análises dos **quantitativos de CT-es entregues**, pendentes e previstos para entrega. 
            No grupo de CT-es entregues, é possível acompanhar o desempenho dos prazos por meio dos indicadores de SLA, considerando tanto 
            a relação entre CT-es entregues e o total de CT-es quanto a relação entre CT-es entregues dentro do prazo e o total de CT-es analisados. 
            \nPara os **CT-es pendentes** (a entregar), a análise é segmentada entre cargas que permanecem dentro do prazo previsto de entrega e cargas 
              que já se encontram atrasadas em relação à data prevista. Além disso, os CT-es pendentes são classificados conforme ocorrências do tipo Cliente, 
               provenientes da operação 930, permitindo identificar situações em que o andamento da entrega depende de ações ou tratativas do cliente. As informações também são distribuídas por Cliente Pagador e Unidade de Destino, 
             da concentração de pendências e dos impactos no cumprimento dos prazos de entrega em cada unidade e carteira de clientes.
            """ )
            st.image("img/Performance_Unidade_GF.png", caption="Gráfico de distribuição BI Performance Unidades.", use_container_width=True)
            st.markdown("""
                    <h5>Modelagem de Dados</h5>""", unsafe_allow_html=True)

    with abas[2]:
        st.header("Performance Região")
        st.markdown("""BI com gráfico barras de análise de % SLA de Entrega por Estado e % SLA Entrega por Vínculo Centro, análise
                    de performance de acordo com Unidade Receptora.  """)
        st.markdown(""" Aqui há uma peculiaridade, as baixas realizadas para o cliente Mercado Livre pela filial SAO deverão receber tratamento específico na visão de retorno.

Dessa forma, quando forem atendidas simultaneamente as seguintes condições:

Código de Baixa do CTRC = 68
Unidade de Entrega = SAO
Data do CTRC igual à Data de Emissão do Romaneio
Os 6 primeiros caracteres do Pagador correspondam a "ebazar"

O registro deverá ser classificado como Baixa, não sendo considerado como Retorno para fins de análise e indicadores da visão.

Essa regra tem como objetivo adequar o tratamento operacional das entregas do Mercado Livre, evitando que movimentações caracterizadas como baixas sejam interpretadas incorretamente como retornos.
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
        st.header("Previsão Entregas - Resumo")

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