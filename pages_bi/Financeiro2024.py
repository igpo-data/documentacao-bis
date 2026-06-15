import streamlit as st
import pandas as pd
import streamlit.components.v1 as components


def render():
    st.title("Faturamento")

    st.info("""
    BI que serve de apuração para o Financeiro, dados advém da 455,467,583. 
    """)

    abas = st.tabs([
        "Tela",
        "Dados",
        ""
    ])

    with abas[0]:
        #st.header("Titulo Grandão")

        st.markdown("""
                    <h5>Visual:</h5>""", unsafe_allow_html=True)
        st.image("img/Financeiro2024.jpg", caption="TVisão da tela de Faturamento", use_container_width=True)

        st.markdown("""
                    <h5>Atualização dos Dados</h5>""", unsafe_allow_html=True)
        st.markdown(""" A rotina de processamento de dados ocorre da seguinte forma:\\
            **Mês Vigente**: A atualização de faturas dos documentos emitidos dentro do mês atual é realizada diariamente.\\
            **Meses Anteriores**: Para documentos emitidos em meses retroativos (com carga histórica de até 90 dias),
            a rotina de atualização é executada aos finais de semana.
            Dessa forma, as informações pendentes serão processadas no final de semana e atualizadas na segunda-feira.  
                     """)
        st.markdown("""
                    <h8>Há pedidos de melhoria deste: atividade 224823 </h8>""", unsafe_allow_html=True)

    with abas[1]:
        st.markdown(""" <h5>Modelagem da base raiz: </h5>""", unsafe_allow_html=True)
        
        tabela = pd.DataFrame({

                    "Procedure": [
                    "atualizar_dim_frete",
                    "atualizar_dim_frete_bkp",
                    "atualizar_dim_frete_updated",
                    "cg_resumo_frete",
                    "cg_tab_dim_frete_e_fato_455",
                    "proc_deletar_duplicada_dim_frete"
                ],

                "O que faz": [
                    "Atualiza a dimensão frete",
                    "Backup da procedure antiga",
                    "Versão mais nova da atualização",
                    "Gera resumo/agregação",
                    "Ambiente de testes",
                    "Remove duplicidades"

                ]})

        st.dataframe(
                    tabela,
                    use_container_width=True,
                    hide_index=True
                )

        st.markdown("""**atualizar_dim_frete ()** """)
        st.markdown("""Ela monta a dim_frete usando as tabelas ssw_op455, ssw_op455_complementar e ssw_op200. 
                    O fluxo que começa pela tabela **ssw_op455**, dentro desta se tem *Serie/Numero CTRC* 
                    e *Data de Emissao*, os quais são concatenados para buscar infos dentro da **ssw_op455_complementar**. Essa última 
                    traz o número do primeiro manifesto (opção 455 complementar A), esse primeiro manifesto é usado para buscar informações 
                    dentro da **ssw_op200**. 
                    \\
                    Da **ssw_op200** (op 200 do SSW) vem dados como DEST_MANIF, HORA_SAIDA_MANIF, DIA_SAIDA_MANIF e EMIS_MANIF. Esses campos
                    ajudam a calcular *operacao_agro*, *op_cvl_hoje*, *data_saida_manifesto* e *data_emissao_manifesto*. 
                    \\
                    Depois disso entra a procedure *atualizar_dim_frete*, junta-se **ssw_op455**, **ssw_op455_complementar** e a *ssw_op200*
                    e verifica se aquele frete já existe na dim_frete, usando *Serie/Numero CTRC*, *Data de Autorizacao*, *Data de Emissao*, se não existe, ela faz 
                    a inserção e o banco gera *sk_dim_frete* se já existe ela faz o update na dim_frete. """) 
        
        st.markdown("""**atualizar_dim_cliente ()** """)
        st.markdown("""A *dim_cliente* vem de duas principais origens, dentro da **ssw_op467** há
                     o cadastro oficial de clientes e na **ssw_op455**
                    são os clientes que aparece nos CT-e/CTRC e tem um complemento. 
                    A base **ssw_op583** traz o CNPJ Principal na *dim_cliente* vem de duas origens principais:\\
                    1. ssw_op467 ↓ cadastro oficial de clientes, alimenta dim_cliente pelo CNPJ/CPF. \
                    
                    2. ssw_op455 ↓ clientes que aparecem nos CT-e/CTRC, alimenta dim_cliente pelos CNPJ's dos fretes. 
                    \\
                    3. ssw_op583 ↓ traz o CNPJ PRINCIPAL 
                    \\
                    O fluxo da procedure **atualizar_dim_cliente()** é:
                    \\
                    ssw_op467 + ssw_op583 ↓ pega o cliente mais recente por CNPJ (Chave: CNPJ/CPF do cliente)
                    \\
                    INSERT/UPDATE na *dim_cliente*\\
                    Depois ela também faz:\\
                    ssw_op455
                            ↓\\
                    busca CNPJ Remetente\\
                    busca CNPJ Pagador\\
                    busca CNPJ Destinatário\\
                    busca CNPJ Expedidor\\
                    busca CNPJ Recebedor ↓ insere na dim_cliente se ainda não existir\\
                    Então, no BI, quando você usa:\\
                    periodicidade =
                    LOOKUPVALUE(
                        dim_cliente[periodicidade],
                        dim_cliente[sk_dim_cliente],
                        dim_frete[sl_cliente_pagador]
                    )\
                    essa periodicidade veio principalmente da:\\
                    ssw_op467 → campo PERIODICIDADE\\
                    E quando usa:
                    cnpj_cliente_pagador =
                    LOOKUPVALUE(
                        dim_cliente[cnpj],
                        dim_cliente[sk_dim_cliente],
                        dim_frete[sl_cliente_pagador]
                    )
                    o CNPJ vem da *dim_cliente*, que pode ter nascido da ssw_op467 ou, 
                    se não existia lá, foi complementada pela ssw_op455.
                    Resumo:
                    ssw_op467 = cadastro oficial do cliente
                    ssw_op583 = CNPJ principal
                    ssw_op455 = fallback operacional dos clientes do frete
                    atualizar_dim_cliente = monta/atualiza dim_cliente
                    dim_cliente = usada no BI para CNPJ e periodicidade
                    1. ssw_op467 cadastro oficial de clientes
                    2. ssw_op455 clientes que aparecem nos CT-e/CTRC
                            
                                        
                     """)


        def render_fluxo_dim_frete():
            html = """
                <section class="fluxo-wrapper">
                    <style>
                        .fluxo-wrapper {
                            font-family: Arial, sans-serif;
                            background: #f7f9fc;
                            padding: 30px;
                            color: #111;
                        }

                        .fluxo-container {
                            display: grid;
                            grid-template-columns: 260px 1fr;
                            gap: 30px;
                            max-width: 1250px;
                            margin: auto;
                        }

                        .indice {
                            background: #ffffff;
                            border-left: 6px solid #062a57;
                            padding: 20px;
                            border-radius: 12px;
                            box-shadow: 0 2px 14px rgba(0,0,0,0.08);
                            height: fit-content;
                            position: sticky;
                            top: 20px;
                        }

                        .indice h3 {
                            color: #062a57;
                            margin-top: 0;
                        }

                        .indice a {
                            display: block;
                            color: #062a57;
                            text-decoration: none;
                            margin: 12px 0;
                            font-weight: bold;
                        }

                        .fluxo {
                            display: flex;
                            flex-direction: column;
                            align-items: center;
                        }

                        .card {
                            width: 500px;
                            background: white;
                            border: 2px solid #062a57;
                            border-radius: 14px;
                            overflow: hidden;
                            box-shadow: 0 4px 14px rgba(0,0,0,0.08);
                        }

                        .card-header {
                            background: #062a57;
                            color: white;
                            padding: 14px;
                            font-size: 20px;
                            font-weight: bold;
                            text-align: center;
                        }

                        .card-body {
                            padding: 20px 30px;
                            font-size: 15px;
                            line-height: 1.5;
                        }

                        .colunas-grid {
                            display: grid;
                            grid-template-columns: 1fr 1fr;
                            gap: 8px 22px;
                            margin-top: 12px;
                        }

                        .coluna {
                            background: #f1f5fb;
                            border-left: 4px solid #062a57;
                            padding: 7px 10px;
                            border-radius: 6px;
                            font-size: 12px;
                        }

                        .arrow {
                            font-size: 34px;
                            color: #062a57;
                            margin: 12px 0;
                        }

                        .join-label {
                            color: #062a57;
                            font-weight: bold;
                            font-size: 15px;
                            margin-bottom: 8px;
                            text-align: center;
                        }

                        .pk {
                            background: #eef3fb;
                            border: 1px dashed #062a57;
                            padding: 8px 12px;
                            border-radius: 8px;
                            display: inline-block;
                            font-weight: bold;
                            color: #062a57;
                        }
                    </style>

                <div class="fluxo-container">

                    <nav class="indice">
                        <h3>Índice do Fluxo</h3>
                        <a href="#ssw455">1. ssw_op455</a>
                        <a href="#complementar">2. ssw_op455_complementar</a>
                        <a href="#op200">3. ssw_op200</a>
                        <a href="#procedure">4. atualizar_dim_frete</a>
                        <a href="#dimfrete">5. dim_frete</a>
                        <a href="#ft455">6. ft_455</a>
                        <a href="#consolidada">7. tab_dim_frete_e_fato_455</a>
                    </nav>

                    <div class="fluxo">

                        <div class="card" id="ssw455">
                            <div class="card-header">1. ssw_op455</div>
                            <div class="card-body">
                                <strong>Base principal do CTRC / CT-e.</strong>
                                <div class="colunas-grid">
                                    <div class="coluna">Serie/Numero CTRC</div>
                                    <div class="coluna">Data de Autorização</div>
                                    <div class="coluna">Data de Emissão</div>
                                    <div class="coluna">Cliente / Unidade</div>
                                    <div class="coluna">Tipo de Frete</div>
                                    <div class="coluna">Tipo de Documento</div>
                                </div>
                            </div>
                        </div>

                        <div class="arrow">↓</div>
                        <div class="join-label">Chave: CTRC + Data de Emissão</div>

                        <div class="card" id="complementar">
                            <div class="card-header">2. ssw_op455_complementar</div>
                            <div class="card-body">
                                <strong>Complementa a 455 com dados operacionais.</strong>
                                <div class="colunas-grid">
                                    <div class="coluna">Primeiro Manifesto</div>
                                    <div class="coluna">Último Manifesto</div>
                                    <div class="coluna">Ocorrência</div>
                                    <div class="coluna">Vendedor</div>
                                    <div class="coluna">Fatura</div>
                                    <div class="coluna">Placa de Entrega</div>
                                </div>
                            </div>
                        </div>

                        <div class="arrow">↓</div>
                        <div class="join-label">Chave: Primeiro Manifesto = NUM_MANIF</div>

                        <div class="card" id="op200">
                            <div class="card-header">3. ssw_op200</div>
                            <div class="card-body">
                                <strong>Base de manifesto.</strong>
                                <div class="colunas-grid">
                                    <div class="coluna">NUM_MANIF</div>
                                    <div class="coluna">DEST_MANIF</div>
                                    <div class="coluna">HORA_SAIDA_MANIF</div>
                                    <div class="coluna">DIA_SAIDA_MANIF</div>
                                    <div class="coluna">EMIS_MANIF</div>
                                </div>
                            </div>
                        </div>

                        <div class="arrow">↓</div>

                        <div class="card" id="procedure">
                            <div class="card-header">4. procedure: atualizar_dim_frete</div>
                            <div class="card-body">
                                <strong>Procedure responsável por montar a dimensão.</strong>
                                <div class="colunas-grid">
                                    <div class="coluna">Junta ssw_op455</div>
                                    <div class="coluna">Junta ssw_op455_complementar</div>
                                    <div class="coluna">Junta ssw_op200</div>
                                    <div class="coluna">Verifica existência na dim_frete</div>
                                    <div class="coluna">Se existir: UPDATE</div>
                                    <div class="coluna">Se não existir: INSERT</div>
                                </div>
                            </div>
                        </div>

                        <div class="arrow">↓</div>

                        <div class="card" id="dimfrete">
                            <div class="card-header">5. tabela:dim_frete</div>
                            <div class="card-body">
                                <p><span class="pk">PK: sk_dim_frete</span></p>
                                <strong>Colunas da dim_frete:</strong>

                                <div class="colunas-grid">
                                    <div class="coluna">Serie/Numero CTRC</div>
                                    <div class="coluna">Data de Autorizacao</div>
                                    <div class="coluna">Data de Emissao</div>
                                    <div class="coluna">Login</div>
                                    <div class="coluna">Placa de Coleta</div>
                                    <div class="coluna">Tipo de Baixa</div>
                                    <div class="coluna">Tipo do Documento</div>
                                    <div class="coluna">Tipo do Frete</div>
                                    <div class="coluna">Tipo de Calculo</div>
                                    <div class="coluna">Unidade Emissora</div>
                                    <div class="coluna">Unidade Receptora</div>
                                    <div class="coluna">Praca Comercial Origem</div>
                                    <div class="coluna">Praca Comercial Destino</div>
                                    <div class="coluna">cod_mercadoria</div>
                                    <div class="coluna">descricao_mercadoria</div>
                                    <div class="coluna">tipo_c_f_t</div>
                                    <div class="coluna">und_expedida</div>
                                    <div class="coluna">assistente</div>
                                    <div class="coluna">unid_repectora</div>
                                    <div class="coluna">tp_calculo_rel_comercial</div>
                                    <div class="coluna">Primeiro Manifesto</div>
                                    <div class="coluna">Ultimo Manifesto</div>
                                    <div class="coluna">Unidade Destino do Ultimo Manifesto</div>
                                    <div class="coluna">Ultimo Romaneio</div>
                                    <div class="coluna">Codigo da Ultima Ocorrencia</div>
                                    <div class="coluna">Descricao da Ultima Ocorrencia</div>
                                    <div class="coluna">Placa de Entrega</div>
                                    <div class="coluna">Numero da Fatura</div>
                                    <div class="coluna">Tipo de Baixa Fatura</div>
                                    <div class="coluna">Vendedor</div>
                                    <div class="coluna">Unidade Origem do Primeiro Manifesto</div>
                                    <div class="coluna">operacao_agro</div>
                                    <div class="coluna">anomes</div>
                                    <div class="coluna">op_cvl_hoje</div>
                                    <div class="coluna">data_saida_manifesto</div>
                                    <div class="coluna">data_emissao_manifesto</div>
                                    <div class="coluna">Cidade de Entrega</div>
                                    <div class="coluna">UF de Entrega</div>
                                    <div class="coluna">CNPJ Remetente</div>
                                    <div class="coluna">Cliente Remetente</div>
                                </div>
                            </div>
                        </div>

                        <div class="arrow">↓</div>
                        <div class="join-label">
                            Ligação: dim_frete.sk_dim_frete = ft_455.sk_dim_frete
                        </div>

                        <div class="card" id="ft455">
                            <div class="card-header">6. tabela: ft_455</div>
                            <div class="card-body">
                                <strong>Tabela fato com valores e medidas.</strong>
                                <div class="colunas-grid">
                                    <div class="coluna">qtd_volumes</div>
                                    <div class="coluna">vlr_mercadoria</div>
                                    <div class="coluna">vlr_frete2</div>
                                    <div class="coluna">Frete Peso</div>
                                    <div class="coluna">Frete Valor</div>
                                    <div class="coluna">Valor do ICMS</div>
                                    <div class="coluna">Pedagio</div>
                                    <div class="coluna">TDE</div>
                                    <div class="coluna">Comissões</div>
                                </div>
                            </div>
                        </div>


                            </div>
                        </div>

                    </div>
                </div>
            </section>
            """

            components.html(html, height=3600, scrolling=True)


        st.set_page_config(
            page_title="Fluxo Dim Frete",
            layout="wide"
        )

        st.markdown("""<h5>Fluxo de Atualização da dim_frete</h5>""", unsafe_allow_html=True)

        render_fluxo_dim_frete()

        st.markdown("""No BI interno foi feito colunas tratadas adjunto a outras bases como a **ft_455** , **dim_cliente**, **clientes_manuais**, **ssw_complementar_455**
                    **base_data_faturamento**, **dim_tempo** e **dim_441**\\
                    \\
                    **Resumo do Tratamento**:\\
                    1. Busca cliente pagador na *ft_455*.\\
                    2. Busca CNPJ e periodicidade na *dim_cliente*.\\
                    3. Verifica regra manual em *clientes_manuais*.\\
                    4. Calcula condição de *faturamento*.\\
                    5. Define data de disponibilidade.\\
                    6. Ajusta disponibilidade para dia útil\\
                    7. Calcula data limite de faturamento.\\
                    8. Verifica se foi faturado no prazo.\\
                    9. Cria ano/mês de faturamento.\\
                    10. Cria código de agrupamento para calendário de faturamento.\\
    

                     """)
                