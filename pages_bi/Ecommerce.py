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
        "NCE Pendentes por Período de Autorização",
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

        st.markdown("""
    <h5>Visão Interativa do Painel de NCE Pendentes</h5> """, unsafe_allow_html=True)
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

                .hotspot.right .tooltip {{
                    left: auto;
                    right: 0;
                }}
            </style>

            <div class="painel">
                <img src="data:image/png;base64,{imagem}">

                <div class="hotspot" style="left:5.1%; top:1.1%; width:31.5%; height:6.1%;">
                    <div class="tooltip">
                        <h3>NCE Pendentes por Período de Autorização</h3>
                        <p>Primeira visão do painel, voltada para acompanhar tudo aquilo que
                        ainda está pendente de entrega. Os filtros, cards, gráficos e tabelas
                        se conectam para detalhar os CTRC's pendentes por cliente, ocorrência,
                        destino e previsão de entrega.</p>
                    </div>
                </div>

                <div class="hotspot" style="left:9.9%; top:8.6%; width:12.0%; height:7.9%;">
                    <div class="tooltip">
                        <h3>Cliente Ecommerce</h3>
                        <p>Filtro usado para separar clientes que são ecommerce ou não, formato de flag. 
                        <code>dim_Pagador (flg_Ecommerce)</code>
                        </p>
                    </div>
                </div>

                <div class="hotspot" style="left:23.2%; top:8.6%; width:11.3%; height:7.9%;">
                    <div class="tooltip">
                        <h3>UF/Destino</h3>
                        <p>Filtro usado para analisar a performance por região ou destino da entrega, 
                         <code>dim_UnidadeReceptora (nom_UF, cod_UnidadeReceptora)</code>
                        </p>
                    </div>
                </div>

                <div class="hotspot" style="left:35.7%; top:8.6%; width:13.7%; height:7.9%;">
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

                <div class="hotspot" style="left:49.9%; top:8.6%; width:12.8%; height:7.9%;">
                    <div class="tooltip">
                        <h3>Status Pendentes</h3>
                        <p>Ajuda a analisar os CT-e pendente, ou seja, aqueles que ainda não estão como entregues, classificados como fora e dentro prazo.
                        <code>fato_FreteExpedidoRecebido (nom_StatusEntregaPendente)</code>
                        </p>
                    </div>
                </div>

                <div class="hotspot" style="left:63.6%; top:8.6%; width:13.8%; height:7.9%;">
                    <div class="tooltip">
                        <h3>Última Ocorrência</h3>
                        <p>Mostra ou filtra pelo último tipo de ocorrência registrada no CT-e.</p>
                    </div>
                </div>

                <div class="hotspot right" style="left:78.3%; top:8.6%; width:13.1%; height:7.9%;">
                    <div class="tooltip">
                        <h3>CTRC</h3>
                        <p>Filtro usado para consultar a situação individual de um CTRC.</p>
                    </div>
                </div>

                <div class="hotspot" style="left:44.5%; top:0.7%; width:14.3%; height:7.2%;">
                    <div class="tooltip">
                        <h3>Período de Autorização</h3>
                        <p>Define o intervalo de autorização usado para a análise dos CTRC's pendentes.
                        <code>dim_PeriodoAutorização(data)</code>
                        </p>
                    </div>
                </div>

                <div class="hotspot" style="left:63.6%; top:2.2%; width:12.3%; height:4.2%;">
                    <div class="tooltip">
                        <h3>Período de Entrega</h3>
                        <p>Alterna a análise temporal para o período de entrega.
                        <code>dim_PeriodoPrevisãoEntrega(data)</code>
                        </p>
                    </div>
                </div>

                <div class="hotspot right" style="left:85.5%; top:1.1%; width:7.5%; height:5.4%;">
                    <div class="tooltip">
                        <h3>Limpar Filtros</h3>
                        <p>Remove os filtros aplicados e retorna o painel para a visão padrão.</p>
                    </div>
                </div>

                <div class="hotspot" style="left:13.1%; top:17.2%; width:14.1%; height:8.0%;">
                    <div class="tooltip">
                        <h3>Rota de Entrega</h3>
                        <p>Card utilizado também como filtro. Ao clicar em Rota de Entrega,
                        o painel passa a mostrar somente os CTRC's pendentes cuja última
                        ocorrência é a 20, ou seja, documentos em saída para entrega.
                        <code>dim_Ocorencia (cod_Ocorrencia, nom_Ocorrencia)</code>
                        
                        </p>
                    </div>
                </div>

                <div class="hotspot" style="left:28.0%; top:17.2%; width:13.0%; height:8.0%;">
                    <div class="tooltip">
                        <h3>Atrasados</h3>
                        <p>Card utilizado também como filtro. Mostra os CTRC's pendentes em que
                        a data de hoje é maior que a data de previsão de entrega. Representa
                        entregas vencidas e ainda não finalizadas.</p>
                    </div>
                </div>

                <div class="hotspot" style="left:42.1%; top:17.2%; width:12.3%; height:8.0%;">
                    <div class="tooltip">
                        <h3>Vencendo Hoje</h3>
                        <p>Card utilizado também como filtro. Mostra os CTRC's pendentes cuja
                        data de previsão de entrega é igual à data de hoje.</p>
                    </div>
                </div>

                <div class="hotspot" style="left:55.2%; top:17.2%; width:13.1%; height:8.0%;">
                    <div class="tooltip">
                        <h3>Vencem Amanhã</h3>
                        <p>Card utilizado também como filtro. Mostra os CTRC's pendentes cuja
                        data de previsão de entrega é amanhã, ou seja, D+1 em relação à data atual.</p>
                    </div>
                </div>

                <div class="hotspot right" style="left:69.5%; top:17.2%; width:13.3%; height:8.0%;">
                    <div class="tooltip">
                        <h3>Vencem em 2 Dias</h3>
                        <p>Card utilizado também como filtro. Mostra os CTRC's pendentes cuja
                        data de previsão de entrega é D+2 em relação à data atual.</p>
                    </div>
                </div>

                <div class="hotspot right" style="left:83.9%; top:17.2%; width:15.3%; height:8.0%;">
                    <div class="tooltip">
                        <h3>Vencem nos próximos 7 dias</h3>
                        <p>Card utilizado também como filtro. Mostra os CTRC's pendentes com
                        previsão de entrega dentro dos próximos 7 dias, considerando a data
                        atual como referência.</p>
                    </div>
                </div>

                <div class="hotspot" style="left:0.5%; top:28.3%; width:28.3%; height:40.0%;">
                    <div class="tooltip">
                        <h3>Gráfico por Cliente</h3>
                        <p>Ranking dos clientes por quantidade de CT-e. Ajuda a identificar os maiores volumes.</p>
                    </div>
                </div>

                <div class="hotspot" style="left:30.1%; top:28.3%; width:42.1%; height:40.4%;">
                    <div class="tooltip">
                        <h3>Gráfico por Ocorrência</h3>
                        <p>Mostra a distribuição dos CT-e por tipo de ocorrência.</p>
                    </div>
                </div>

                <div class="hotspot right" style="left:73.0%; top:28.3%; width:26.1%; height:40.4%;">
                    <div class="tooltip">
                        <h3>Tabela por Destino</h3>
                        <p>Mostra indicadores por destino: total de CT-e, em rota, no prazo e
                        fora do prazo. Quando aparecer No Prazo (não roter.) ou Fora do Prazo
                        (não roter.), significa que o CTRC está dentro daquela condição de prazo,
                        mas ainda não foi roteirizado para entrega.</p>
                    </div>
                </div>

                <div class="hotspot right" style="left:1.2%; top:72.4%; width:97.9%; height:26.4%;">
                    <div class="tooltip">
                        <h3>Tabela de Exportação</h3>
                        <p>Lista os CT-e detalhados com destino, ocorrência, previsão de entrega e destinatário. </p>
                    </div>
                </div>
            </div>
            """

            components.html(html, height=900, scrolling=True)

        def render_card_filtro(nome, imagem_path, left, width, descricao, right=False):
            if not Path(imagem_path).exists():
                imagem_path = "img/ecommerce_nce.PNG"

            imagem = img_to_base64(imagem_path)
            classe = "hotspot right" if right else "hotspot"

            html = f"""
            <style>
                .painel-card {{
                    position: relative;
                    width: 100%;
                    max-width: 1550px;
                    margin: auto;
                }}

                .painel-card img {{
                    width: 100%;
                    border-radius: 8px;
                }}

                .hotspot {{
                    position: absolute;
                    cursor: pointer;
                    border: 3px solid #00BFFF;
                    background: rgba(0,191,255,0.12);
                    box-shadow: 0 0 10px rgba(0,191,255,0.55);
                    transition: 0.2s;
                }}

                .hotspot:hover {{
                    background: rgba(0,191,255,0.24);
                    box-shadow: 0 0 18px rgba(0,191,255,0.85);
                }}

                .tooltip {{
                    visibility: hidden;
                    opacity: 0;
                    position: absolute;
                    z-index: 9999;
                    width: 390px;
                    background: white;
                    color: #333;
                    border-radius: 14px;
                    padding: 16px;
                    box-shadow: 0 8px 24px rgba(0,0,0,0.30);
                    font-family: Arial, sans-serif;
                    top: 110%;
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

                .hotspot.right .tooltip {{
                    left: auto;
                    right: 0;
                }}
            </style>

            <div class="painel-card">
                <img src="data:image/png;base64,{imagem}">
                <div class="{classe}" style="left:{left}%; top:17.2%; width:{width}%; height:8.0%;">
                    <div class="tooltip">
                        <h3>{nome}</h3>
                        <p>{descricao}</p>
                    </div>
                </div>
            </div>
            """

            components.html(html, height=900, scrolling=True)

        def render_documentacao_cards():
            st.markdown("""
            <h5>Cards como filtros do painel</h5>
            """, unsafe_allow_html=True)
            st.info(
                "Esta visão é voltada para CTRC's pendentes de entrega. "
                "Os cards funcionam como filtros: ao clicar em um card no Power BI, "
                "todos os visuais passam a considerar somente a regra daquele card."
            )

            cards = [
                {
                    "nome": "Rota de Entrega",
                    "imagem": "img/Ecommerce_RE.jpg",
                    "left": 13.1,
                    "width": 14.1,
                    "right": False,
                    "descricao": (
                        "Filtra os CTRC's pendentes cuja última ocorrência é a 20. "
                        "Na prática, são documentos que já foram roteirizados e estão "
                        "em saída para entrega."
                    ),
                },
                {
                    "nome": "Atrasados",
                    "imagem": "img/Ecommerce_Atrasados.jpg",
                    "left": 28.0,
                    "width": 13.0,
                    "right": False,
                    "descricao": (
                        "Filtra os CTRC's pendentes em que a data de hoje é maior que "
                        "a data de previsão de entrega. São entregas vencidas e ainda "
                        "não finalizadas."
                    ),
                },
                {
                    "nome": "Vencendo Hoje",
                    "imagem": "img/Ecommerce_VencendoH.jpg",
                    "left": 42.1,
                    "width": 12.3,
                    "right": False,
                    "descricao": (
                        "Filtra os CTRC's pendentes cuja data de previsão de entrega "
                        "é igual à data de hoje."
                    ),
                },
                {
                    "nome": "Vencem Amanhã",
                    "imagem": "img/Ecommerce_VencemA.jpg",
                    "left": 55.2,
                    "width": 13.1,
                    "right": False,
                    "descricao": (
                        "Filtra os CTRC's pendentes cuja data de previsão de entrega "
                        "é amanhã, ou seja, D+1 em relação à data atual."
                    ),
                },
                {
                    "nome": "Vencem em 2 Dias",
                    "imagem": "img/Ecommerce_Vencem2.jpg",
                    "left": 69.5,
                    "width": 13.3,
                    "right": True,
                    "descricao": (
                        "Filtra os CTRC's pendentes cuja data de previsão de entrega "
                        "é D+2 em relação à data atual."
                    ),
                },
                {
                    "nome": "Vencem nos Próximos 7 dias",
                    "imagem": "img/Ecommerce_Vencem7.jpg",
                    "left": 83.9,
                    "width": 15.3,
                    "right": True,
                    "descricao": (
                        "Filtra os CTRC's pendentes com previsão de entrega dentro dos "
                        "próximos 7 dias, considerando a data atual como referência."
                    ),
                },
            ]

            for card in cards:
                with st.expander(card["nome"]):
                    render_card_filtro(
                        card["nome"],
                        card["imagem"],
                        card["left"],
                        card["width"],
                        card["descricao"],
                        card["right"],
                    )

        render_ecommerce_interativo()
        render_documentacao_cards()
        st.markdown(""" Ocorrência do Painel: 
                    \\
        Há ocorrencias que são retiradas da visualização do painel, como            
        **Tipo: Cliente** 
                    \\
        AGUARD. AUTORIZACAO PARA DEV. -> 32 
                    \\
        MERCADORIA CONFISCADA PELA FISCALIZACAO -> 66
                    \\
        **Tipo: Pendência**
                    \\
        MERCADORIA EM INDENIZACAO -> 48
                    \\
        **Tipo: Baixa**
        CTRC BAIXADO / CANCELADO ->83
                    \\
        CONHECIMENTO SUBSTITUIDO->87
                    \\
        DEVOLUCAO RECUSA TOTAL -> 61
                    \\
        DEVOLUCAO RECUSA PARCIAL -> 62
                    \\
        MERCADORIA INDENIZADA -> 94
                    \\
        CTRC PARA EFEITO DE FRETE ->97
                    \\
        BAIXA AUTORIZADA DIRETORIA -> 39
                    \\
        **Tipo: Informativo** 
                    \\
        ANEXADO COMPROVANTE DE ENTREGA COMPLEMENTAR -> 76
     """)
    with abas[2]:
        st.markdown("### Analítico de Quantidade e Valor de CTE")

        st.markdown("""
        Esta tela apresenta a análise do quantitativo de CTRC/CT-e e do valor do frete bruto,
        permitindo acompanhar o comportamento da operação por período, unidade, cliente e demais
        dimensões disponíveis no painel.

        A visão foi estruturada em duas perspectivas:

        - **Visão por Autorização:** considera a data de autorização do CT-e como referência temporal.
        - **Visão por Entrega:** considera a data de entrega como referência temporal.

        Dessa forma, o usuário consegue avaliar tanto o volume autorizado quanto o volume efetivamente
        entregue, além de comparar o comportamento do frete bruto dentro de cada contexto de análise.
        """)

        col_aut, col_ent = st.columns(2)

        with col_aut:
            st.markdown("#### Visão Autorização")
            st.image(
                "img/Ecommerce_AnaliticoAutorizacao.jpg",
                caption="Analítico de Quantidade e Valor de CTE - Autorização",
                use_container_width=True,
            )

        with col_ent:
            st.markdown("#### Visão Entrega")
            st.image(
                "img/Ecommerce_AnaliticoEntrega.jpg",
                caption="Analítico de Quantidade e Valor de CTE - Entrega",
                use_container_width=True,
            )

        st.divider()

        st.markdown("### Melhoria – Identificação de Outliers Operacionais")

        st.markdown("""
        #### Objetivo

        Foi implementada uma melhoria no BI para permitir a identificação automática de comportamentos
        atípicos na **Quantidade de CT-e** e no **Valor do Frete Bruto**, auxiliando o time Comercial
        na detecção de alterações significativas no volume de movimentação das unidades.

        O principal objetivo é evidenciar aumentos expressivos que possam indicar mudanças operacionais,
        aquisição de novos clientes, absorção de demanda de outras transportadoras ou qualquer outro
        evento que provoque um crescimento fora do padrão histórico.

        #### Critério de Comparação

        Como referência histórica, foi adotada a **mediana do mesmo mês do ano anterior**.
        """)

        st.table(pd.DataFrame({
            "Período analisado": ["Junho/2026", "Julho/2026", "Agosto/2026"],
            "Referência utilizada": [
                "Mediana diária de Junho/2025",
                "Mediana diária de Julho/2025",
                "Mediana diária de Agosto/2025",
            ],
        }))

        st.markdown("""
        Essa abordagem permite comparar períodos equivalentes, reduzindo impactos causados por sazonalidade.

        #### Justificativa da utilização da Mediana

        Foi utilizada a mediana em vez da média por representar melhor o comportamento típico da operação.

        A mediana possui menor influência de valores extremamente altos ou baixos (*outliers*), tornando
        a comparação mais estável e confiável para análise operacional. Dessa forma, eventos isolados não
        distorcem o valor de referência utilizado pelo indicador.

        #### Medidas Implementadas

        **Mediana CT-e Mesmo Mês Ano Anterior**

        Calcula a mediana da Quantidade de CT-e considerando todos os dias do mesmo mês do ano anterior.

        **Objetivo:** estabelecer uma referência histórica para comparação com o período atual.

        **Índice de Crescimento CT-e**

        Calcula o percentual de crescimento da Quantidade de CT-e em relação à mediana histórica.

        Fórmula utilizada:

        `Índice de Crescimento = (Quantidade CT-e Atual - Mediana Histórica) / Mediana Histórica`
        """)

        st.table(pd.DataFrame({
            "Resultado": ["0%", "20%", "80%", "100%", "-15%"],
            "Significado": [
                "Igual à mediana",
                "20% acima da mediana",
                "80% acima da mediana",
                "Volume equivalente ao dobro da mediana",
                "15% abaixo da mediana",
            ],
        }))

        st.markdown("""
        **Indicador Visual (Cor Crescimento CT-e)**

        Foi criado um indicador responsável por destacar visualmente os registros cujo crescimento seja
        considerado significativo.

        Critério utilizado:

        - crescimento inferior a **80%** → indicador normal;
        - crescimento igual ou superior a **80%** → destaque visual em amarelo.

        Esse recurso facilita a identificação imediata de unidades ou períodos com crescimento acima do
        comportamento histórico esperado.

        #### Valor do Frete Bruto

        A mesma metodologia foi aplicada ao indicador de **Valor do Frete Bruto**.

        Foram desenvolvidas as seguintes medidas:

        - Mediana do Valor do Frete do mesmo mês do ano anterior;
        - Índice de Crescimento do Valor do Frete;
        - Indicador visual de crescimento superior a 80%.

        Assim, além do volume de CT-e, também é possível identificar variações relevantes no faturamento
        operacional.

        #### Benefícios da Melhoria

        - Identificação rápida de outliers operacionais.
        - Comparação baseada em períodos equivalentes, respeitando a sazonalidade.
        - Maior confiabilidade estatística devido ao uso da mediana.
        - Destaque automático de crescimentos relevantes.
        - Apoio ao time Comercial na identificação de oportunidades, mudanças de mercado e alterações de comportamento das unidades.
        - Redução da necessidade de análises manuais para localizar crescimentos expressivos.
        """)

        with st.expander("Medidas DAX - Visão Autorização"):
            st.code("""
Mediana CT-e Mesmo Mês Ano Anterior_Autorizacao =
VAR DataReferencia =
    MAX('dim_PeriodoAutorizacao'[Data])

VAR InicioMesAnoAnterior =
    DATE(
        YEAR(DataReferencia) - 1,
        MONTH(DataReferencia),
        1
    )

VAR FimMesAnoAnterior =
    EOMONTH(InicioMesAnoAnterior, 0)

RETURN
MEDIANX(
    FILTER(
        ALL('dim_PeriodoAutorizacao'[Data]),
        'dim_PeriodoAutorizacao'[Data] >= InicioMesAnoAnterior &&
        'dim_PeriodoAutorizacao'[Data] <= FimMesAnoAnterior
    ),
    CALCULATE([Quantidade CT-e])
)

Índice Crescimento CT-e Autorizacao =
DIVIDE(
    [Quantidade CT-e] - [Mediana CT-e Mesmo Mês Ano Anterior_Autorizacao],
    [Mediana CT-e Mesmo Mês Ano Anterior_Autorizacao]
)

Cor Crescimento CT-e Aut =
IF(
    [Índice Crescimento CT-e Autorizacao] >= 0.8,
    1,
    0
)

Mediana Vlr_Frete Mesmo Mês Ano Anterior_Aut =
VAR DataReferencia =
    MAX('dim_PeriodoAutorizacao'[Data])

VAR InicioMesAnoAnterior =
    DATE(
        YEAR(DataReferencia) - 1,
        MONTH(DataReferencia),
        1
    )

VAR FimMesAnoAnterior =
    EOMONTH(InicioMesAnoAnterior, 0)

RETURN
MEDIANX(
    FILTER(
        ALL('dim_PeriodoAutorizacao'[Data]),
        'dim_PeriodoAutorizacao'[Data] >= InicioMesAnoAnterior &&
        'dim_PeriodoAutorizacao'[Data] <= FimMesAnoAnterior
    ),
    CALCULATE([Valor Frete Bruto])
)

Índice Crescimento Valor Frete_AUT =
DIVIDE(
    [Valor Frete Bruto] - [Mediana Vlr_Frete Mesmo Mês Ano Anterior_Aut],
    [Mediana Vlr_Frete Mesmo Mês Ano Anterior_Aut]
)

Cor Crescimento Frete_Aut =
IF(
    [Índice Crescimento Valor Frete_AUT] >= 0.8,
    1,
    0
)
""", language="DAX")

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


