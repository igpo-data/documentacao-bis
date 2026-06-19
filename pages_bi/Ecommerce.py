import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import base64
from pathlib import Path


def render():
    st.title("E-commerce")

    st.info("""
     BI que tem como principal objetivo a análise do Núcleo de Clientes Especiais com uma flag para aquele que também são E-Commerce. Lembrar
    que todo E-commerce é NCE, porém nem todo NCE é E-commerce. Ex: John Deere. 
    """)

    abas = st.tabs([
        "E-commerce",
        "Visão Geral",
        "Analítico de Quantidade e Valor de CTE",
        "Previsão de Entregas",
        "Visão Mapas",
        "Por Cliente",
        "SLA Por Cliente",
        "Analítico", 
        "Modelagem e Extração"
    ])

    with abas[0]:
        def img_to_base64(path):
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
                    border: 3px solid #00BFFF;
                    background: rgba(0,191,255,0.15);
                    box-shadow: 0 0 14px rgba(0,191,255,0.8);
                }}

                .tooltip {{
                    visibility: hidden;
                    opacity: 0;
                    position: absolute;
                    z-index: 9999;
                    width: 360px;
                    background: white;
                    color: #333;
                    border-radius: 14px;
                    padding: 16px;
                    box-shadow: 0 8px 24px rgba(0,0,0,0.30);
                    font-family: Arial, sans-serif;
                    top: 105%;
                    left: 0;
                    transition: opacity 0.25s ease;
                }}

                .tooltip h3 {{
                    margin-top: 0;
                    color: #0b4f8a;
                    font-size: 18px;
                }}

                .tooltip p {{
                    font-size: 14px;
                    line-height: 1.45;
                    margin-bottom: 0;
                }}

                .hotspot:hover .tooltip {{
                    visibility: visible;
                    opacity: 1;
                }}
            </style>

            <div class="painel">
                <img src="data:image/png;base64,{imagem}">

                <div class="hotspot" style="left:0.3%; top:8.8%; width:12.3%; height:8.4%;">
                    <div class="tooltip">
                        <h3>Cliente Ecommerce</h3>
                        <p>Filtro usado para separar clientes que são ecommerce ou não, formato de flag. 
                        <code>dim_Pagador (flg_Ecommerce)</code>
                        </p>
                    </div>
                </div>

                <div class="hotspot" style="left:13.7%; top:9.2%; width:11.4%; height:7.8%;">
                    <div class="tooltip">
                        <h3>UF/Destino</h3>
                        <p>Filtro usado para analisar a performance por região ou destino da entrega.
                         <code>dim_UnidadeReceptora (nom_UF, cod_UnidadeReceptora)</code>
                        </p>
                    </div>
                </div>

                <div class="hotspot" style="left:26.2%; top:9.2%; width:13.6%; height:7.8%;">
                    <div class="tooltip">
                        <h3>Cliente</h3>
                        <p>Permite selecionar um cliente específico e visualizar os indicadores apenas dele.
                        Modelagem: há uma lista de clientes que são participantes do Núcleo de Clientes Especiais essa
                        relação é configurada de maneira manual em uma planilha no sheerpoint. 
                        <code>dim_Pagador (nom_ClienteNCE)</code>
                        </p>
                        </p>
                    </div>
                </div>

                <div class="hotspot" style="left:41.3%; top:9.2%; width:14.8%; height:7.8%;">
                    <div class="tooltip">
                        <h3>Situação Entrega</h3>
                        <p>Filtro para separar dentroa dos CTRC'S entregues  os que estão fora e dentro do prazo.
                        <code>fato_FreteExpedidoRecebido (nom_StatusEntrega)</code>
                        </p>
                    </div>
                </div>

                <div class="hotspot" style="left:57.2%; top:9.2%; width:12.9%; height:7.8%;">
                    <div class="tooltip">
                        <h3>Status Pendentes</h3>
                        <p>Ajuda a analisar os CT-e pendente, ou seja, aqueles que ainda não estão como entregues, classificados como fora e dentro prazo.
                        <code>fato_FreteExpedidoRecebido (nom_StatusEntregaPendente)</code>
                        </p>
                    </div>
                </div>

                <div class="hotspot" style="left:70.9%; top:9.2%; width:13.7%; height:7.8%;">
                    <div class="tooltip">
                        <h3>Última Ocorrência</h3>
                        <p>Mostra ou filtra pelo último tipo de ocorrência registrada no CT-e.</p>
                    </div>
                </div>

                <div class="hotspot" style="left:85.7%; top:9.2%; width:13%; height:7.8%;">
                    <div class="tooltip">
                        <h3>CTRC</h3>
                        <p>Filtro usado para consultar a situação individual de uma entrega.</p>
                    </div>
                </div>

                <div class="hotspot" style="left:38.5%; top:0.8%; width:15.3%; height:6%;">
                    <div class="tooltip">
                        <h3>Filtro de Previsão de Entrega</h3>
                        <p> Esse período é mesmo encontrado nos paineis de performance geral
                        <code>dim_PeriodoPrevisãoEntrega(data)</code>
                        </p>
                    </div>
                </div>

                <div class="hotspot" style="left:55.9%; top:2.8%; width:17%; height:4.5%;">
                    <div class="tooltip">
                        <h3>Período de Autorização</h3>
                        <p>Alterna a análise temporal para o período de autorização advindo da 455. 
                        <code>dim_PeriodoAutorização(data)</code>
                        </p>
                    </div>
                </div>

                <div class="hotspot" style="left:85.8%; top:1.5%; width:7.5%; height:5.2%;">
                    <div class="tooltip">
                        <h3>Limpar Filtros</h3>
                        <p>Remove os filtros aplicados e retorna o painel para a visão padrão.</p>
                    </div>
                </div>

                <div class="hotspot" style="left:13%; top:17%; width:14%; height:8%;">
                    <div class="tooltip">
                        <h3>Rota de Entrega</h3>
                        <p>Mostra a quantidade de CT-e que estão em rota de entrega,
                        considerando a última ocorrência operacional registrada para o documento.
                        <code>dim_Ocorencia (cod_Ocorrencia, nom_Ocorrencia)</code>
                        
                        </p>
                    </div>
                </div>

                <div class="hotspot" style="left:28%; top:17%; width:13%; height:8%;">
                    <div class="tooltip">
                        <h3>Atrasados</h3>
                        <p>Quantidade de CTRC's pendentes cuja previsão de entrega é anterior à data atual.
                        Representa entregas vencidas e ainda não finalizadas.</p>
                    </div>
                </div>

                <div class="hotspot" style="left:42%; top:17%; width:13%; height:8%;">
                    <div class="tooltip">
                        <h3>Vencendo Hoje</h3>
                        <p>Quantidade de CTRC's pendentes com previsão de entrega igual à data atual.</p>
                    </div>
                </div>

                <div class="hotspot" style="left:56%; top:17%; width:13%; height:8%;">
                    <div class="tooltip">
                        <h3>Vencem Amanhã</h3>
                        <p>Quantidade de CTRC's pendentes com previsão de entrega para D+1,
                        ou seja, o próximo dia em relação à data atual.</p>
                    </div>
                </div>

                <div class="hotspot" style="left:70%; top:17%; width:13%; height:8%;">
                    <div class="tooltip">
                        <h3>Vencem em 2 Dias</h3>
                        <p>Quantidade de CTRC's pendentes com previsão de entrega para D+2.</p>
                    </div>
                </div>

                <div class="hotspot" style="left:84%; top:17%; width:15%; height:8%;">
                    <div class="tooltip">
                        <h3>Vencem nos próximos 7 dias</h3>
                        <p>Quantidade de CTRC's pendentes com previsão de entrega dentro dos próximos
                        7 dias, considerando a data atual como referência.</p>
                    </div>
                </div>

                <div class="hotspot" style="left:0.5%; top:28%; width:32%; height:39%;">
                    <div class="tooltip">
                        <h3>Gráfico por Cliente</h3>
                        <p>Ranking dos clientes por quantidade de CT-e. Ajuda a identificar os maiores volumes.</p>
                    </div>
                </div>

                <div class="hotspot" style="left:34%; top:28%; width:33%; height:39%;">
                    <div class="tooltip">
                        <h3>Gráfico por Ocorrência</h3>
                        <p>Mostra a distribuição dos CT-e por tipo de ocorrência.</p>
                    </div>
                </div>

                <div class="hotspot" style="left:68%; top:28%; width:31%; height:39%;">
                    <div class="tooltip">
                        <h3>Tabela por Destino</h3>
                        <p>Mostra indicadores por destino: total de CT-e, em rota, no prazo, fora do prazo e SLA.</p>
                    </div>
                </div>

                <div class="hotspot" style="left:0.5%; top:72%; width:98%; height:26%;">
                    <div class="tooltip">
                        <h3>Tabela de Exportação</h3>
                        <p>Lista os CT-e detalhados com destino, ocorrência, previsão de entrega e destinatário. </p>
                    </div>
                </div>
            </div>
            """

            components.html(html, height=900, scrolling=True)


        render_ecommerce_interativo()
     st.markdown(""" Ocorrência do Painel: 
                    \\
        Há ocorrencias que são retiradas da visualização do painel, como            
        **Tipo: Cliente** 
        AGUARD. AUTORIZACAO PARA DEV. -> 32 
        MERCADORIA CONFISCADA PELA FISCALIZACAO -> 66
        **Tipo: Pendência**
        MERCADORIA EM INDENIZACAO -> 48
                    \\
        **Tipo: Baixa**
        CTRC BAIXADO / CANCELADO ->83
        CONHECIMENTO SUBSTITUIDO->87
        DEVOLUCAO RECUSA TOTAL -> 61
        DEVOLUCAO RECUSA PARCIAL -> 62
        MERCADORIA INDENIZADA -> 94
        CTRC PARA EFEITO DE FRETE ->97
        BAIXA AUTORIZADA DIRETORIA -> 39
                    \\
        **Tipo: Informativo** 
        ANEXADO COMPROVANTE DE ENTREGA COMPLEMENTAR -> 76
     """)
    with abas[8]:
        st.markdown("""Nesse BI é feito pela extração da 455 junto com a sua complementar A, sendo as colunas necessárias: 
        - Serie/Numero CTRC : Comtemplar a tabela de exportação, medida de soma de quantidade de CTRC dentro do período e constitui filtro. 
        \\
        - Cliente Destinatário: Comtemplar a tabela de exportação e dentro da modelagem a dim_Destinatario
        \\
        - Cidade Destino: Comtemplar a tabela de exportação e dentro da modelagem a dim_Destinatario
        \\
        - Unidade de Destino: Comtemplar a tabela de exportação e dentro da modelagem a dim_Destinatario
        \\
        - Data de hoje - Previsão de entrega = Atraso do CTRC. Nessa contexto formatação da dim_Previsão de Entrega aqui. 
                    
                     """)
