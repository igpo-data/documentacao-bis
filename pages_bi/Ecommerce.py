import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import base64
from pathlib import Path


def render():
    st.title("E-commerce")

    st.info("""
     BI que tem como principal objetivo a análise dos clientes que são do NCE,com uma flag para aquele que também são E-Commerce. 
    """)

    abas = st.tabs([
        "E-commerce",
        "Visão Geral",
        "Analítico de Quantidade e Valor de CTE",
        "Previsão de Entregas",
        "Visão Mapas",
        "Por Cliente",
        "SLA Por Cliente",
        "Analítico"
    ])

    with abas[0]:
        def img_to_base64(path):
        #def img_to_base64(path):
            return base64.b64encode(Path(path).read_bytes()).decode()

        def render_ecommerce_interativo():
            imagem = img_to_base64("img/ecommerce_nce.PNG")

            html = f"""
            <style>
                .painel {{
                    position: relative;
                    width: 100%;
                    max-width: 1550px;
                    margin: auto;
                }}

                .painel img {{
                    width: 100%;
                    border-radius: 8px;
                }}

                .hotspot {{
                    position: absolute;
                    cursor: pointer;
                    border: 2px solid transparent;
                    transition: 0.2s;
                }}

                .hotspot:hover {{
                    border: 3px solid #ffcc00;
                    background: rgba(255, 204, 0, 0.18);
                    box-shadow: 0 0 14px rgba(255, 204, 0, 0.8);
                }}

                .modal {{
                    display: none;
                    position: fixed;
                    z-index: 9999;
                    left: 0;
                    top: 0;
                    width: 100%;
                    height: 100%;
                    background: rgba(0,0,0,0.70);
                    align-items: center;
                    justify-content: center;
                }}

                .modal-box {{
                    background: white;
                    width: 520px;
                    max-width: 90%;
                    border-radius: 18px;
                    padding: 28px;
                    box-shadow: 0 18px 45px rgba(0,0,0,0.45);
                    animation: abrir 0.35s ease;
                    font-family: Arial, sans-serif;
                }}

                .modal-box h2 {{
                    margin-top: 0;
                    color: #0b4f8a;
                }}

                .modal-box p {{
                    font-size: 16px;
                    line-height: 1.5;
                    color: #333;
                }}

                .close {{
                    float: right;
                    font-size: 26px;
                    cursor: pointer;
                    color: #555;
                }}

                @keyframes abrir {{
                    from {{
                        transform: scale(0.65);
                        opacity: 0;
                    }}
                    to {{
                        transform: scale(1);
                        opacity: 1;
                    }}
                }}
            </style>

            <div class="painel">
                <img src="data:image/png;base64,{imagem}">

                <!-- FILTROS  -->

                <div class="hotspot" onclick="abrirModal('Cliente Ecommerce', 'Filtro usado para separar clientes que são ou não são ecommerce. Permite analisar apenas operações ecommerce ou comparar com clientes não ecommerce.')" style="left:0.3%; top:8.8%; width:12.3%; height:8.4%;"></div>

                <div class="hotspot" onclick="abrirModal('UF/Destino', 'Filtro usado para selecionar a unidade federativa ou destino da entrega. Ajuda a analisar a performance por região de destino.')" style="left:13.7%; top:9.2%; width:11.4%; height:7.8%;"></div>

                <div class="hotspot" onclick="abrirModal('Cliente', 'Filtro usado para selecionar um cliente específico e visualizar os indicadores apenas daquele cliente.')" style="left:26.2%; top:9.2%; width:13.6%; height:7.8%;"></div>

                <div class="hotspot" onclick="abrirModal('Situação Entrega', 'Filtro usado para separar entregas conforme a situação operacional, como em rota, atrasadas, vencendo hoje ou entregas previstas.')" style="left:41.3%; top:9.2%; width:14.8%; height:7.8%;"></div>

                <div class="hotspot" onclick="abrirModal('Status Pendentes', 'Filtro usado para analisar CT-e pendentes conforme o status de prazo, permitindo focar no que está no prazo, fora do prazo ou próximo do vencimento.')" style="left:57.2%; top:9.2%; width:12.9%; height:7.8%;"></div>

                <div class="hotspot" onclick="abrirModal('Última Ocorrência', 'Filtro usado para selecionar o tipo da última ocorrência registrada no CT-e. Ajuda a entender o motivo operacional mais recente da entrega.')" style="left:70.9%; top:9.2%; width:13.7%; height:7.8%;"></div>

                <div class="hotspot" onclick="abrirModal('CTRC', 'Filtro usado para pesquisar um CTRC específico e consultar a situação individual da entrega.')" style="left:85.7%; top:9.2%; width:13%; height:7.8%;"></div>

                <div class="hotspot" onclick="abrirModal('Período de Previsão de Entrega', 'Filtro de datas usado para definir o intervalo de previsão de entrega analisado no painel.')" style="left:38.5%; top:0.8%; width:15.3%; height:6%;"></div>

                <div class="hotspot" onclick="abrirModal('Período de Autorização', 'Botão usado para alternar ou aplicar análise pelo período de autorização, mudando a lógica temporal do painel.')" style="left:55.9%; top:2.8%; width:17%; height:4.5%;"></div>

                <div class="hotspot" onclick="abrirModal('Limpar Filtros', 'Botão usado para remover os filtros aplicados e retornar o painel para a visão padrão.')" style="left:85.8%; top:1.5%; width:7.5%; height:5.2%;"></div>

                <!-- CARDS SUPERIORES -->
                <div class="hotspot" onclick="abrirModal('Rota de Entrega', 'Mostra a quantidade de CT-e que estão em rota de entrega no período selecionado.')" style="left:13%; top:17%; width:14%; height:8%;"></div>

                <div class="hotspot" onclick="abrirModal('Atrasados', 'Mostra a quantidade de entregas que estão fora do prazo previsto.')" style="left:28%; top:17%; width:13%; height:8%;"></div>

                <div class="hotspot" onclick="abrirModal('Vencendo Hoje', 'Mostra os CT-e cuja previsão de entrega vence no dia atual.')" style="left:42%; top:17%; width:13%; height:8%;"></div>

                <div class="hotspot" onclick="abrirModal('Vencem Amanhã', 'Mostra os CT-e com previsão de entrega para o próximo dia.')" style="left:56%; top:17%; width:13%; height:8%;"></div>

                <div class="hotspot" onclick="abrirModal('Vencem em 2 Dias', 'Mostra os CT-e que ainda possuem dois dias até o vencimento da previsão de entrega.')" style="left:70%; top:17%; width:13%; height:8%;"></div>

                <div class="hotspot" onclick="abrirModal('Vencem essa Semana', 'Mostra o total de CT-e que vencem dentro da semana atual.')" style="left:84%; top:17%; width:15%; height:8%;"></div>

                <!-- GRÁFICOS -->
                <div class="hotspot" onclick="abrirModal('Gráfico por Cliente', 'Ranking dos clientes por quantidade de CT-e. Ajuda a identificar quais clientes concentram maior volume de entregas.')" style="left:0.5%; top:28%; width:32%; height:39%;"></div>

                <div class="hotspot" onclick="abrirModal('Gráfico por Ocorrência', 'Mostra a distribuição dos CT-e por tipo de ocorrência. Ajuda a entender os principais motivos de pendência ou atraso.')" style="left:34%; top:28%; width:33%; height:39%;"></div>

                <!-- TABELA DESTINO -->
                <div class="hotspot" onclick="abrirModal('Tabela por Destino', 'Mostra os indicadores por unidade de destino, incluindo total de CT-e, em rota, no prazo, fora do prazo e percentual de SLA.')" style="left:68%; top:28%; width:31%; height:39%;"></div>

                <!-- TABELA INFERIOR -->
                <div class="hotspot" onclick="abrirModal('Tabela Analítica', 'Lista os CT-e detalhados com destino, código da ocorrência, data da última ocorrência, previsão de entrega e destinatário.')" style="left:0.5%; top:72%; width:98%; height:26%;"></div>
            </div>

            <div id="modal" class="modal" onclick="fecharModal()">
                <div class="modal-box" onclick="event.stopPropagation()">
                    <span class="close" onclick="fecharModal()">&times;</span>
                    <h2 id="titulo"></h2>
                    <p id="texto"></p>
                </div>
            </div>

            <script>
                function abrirModal(titulo, texto) {{
                    document.getElementById("titulo").innerText = titulo;
                    document.getElementById("texto").innerText = texto;
                    document.getElementById("modal").style.display = "flex";
                }}

                function fecharModal() {{
                    document.getElementById("modal").style.display = "none";
                }}
            </script>
            """

            components.html(html, height=900, scrolling=True)


        render_ecommerce_interativo()