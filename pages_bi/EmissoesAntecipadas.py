import streamlit as st
import pandas as pd
import streamlit.components.v1 as components


def render():
    st.title("Emissões Antecipadas")

    st.info("""
    Este BI tem por finalidade o calculo do Prêmio Superação
            \n 
            Base: 915 e 206. 
    """)

    abas = st.tabs([
        "Modo de Extração/ Dados",
        "BI"
    ])
    
    with abas[0]:
        st.markdown("""
                            <h5>Modo de extração</h5>""", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)

        with col1:
                st.image("img/Tela206.jpg", caption="Tela de Extração da 206", use_container_width=True)

        with col2:
            st.image("img/Tela915.jpg", caption="Tela de Extração da 915 ", use_container_width=True)
        
        st.markdown("""**Obs**: A tela de extração da 915 muda momentaneamente, sendo o formato de tela como o da imagem, contendo a opção tipo de dados: CTRC e Fatura. 
                    \n 
                    Outro Ponto, a extração da tabela 915 é feita pelo Período de Autorização com o periodo máximo de 31 dias e se preenche quando se escolhe CTRC's
                    em Tipo de Dados.  
                            """)

        st.markdown("""
                            <h5>Dados Brutos.</h5>""", unsafe_allow_html=True)
        
       ########### tabela de exemplo 
    st.markdown("""**Mapeamento da 206** """)
    
    tabela206 = pd.DataFrame({

                    " Nome ": [
                    "NF-E",
                    "CHAVE DANFE",
                    "XML",
                    "NR1/NR2",
                    "CTR"
                ],

                "Descrição": [
                    "Número da Nota Fiscal.",
                    "Chave pode ser copiada com Ctrl-V e colada com Ctrl-C na opção 004 para gerar o CT-e correspondente.",
                    "O S indica que o XML da DANFE está disponível, o que facilita a geração do CT-e.",
                    "Etiquetas sequenciais dos volumes coletados utilizadas para descarregamento com SSWBar.",
                    "S indica que no momento da geração do relatório o pré-CTRC já se encontra emitido."
                ],

            })
    st.markdown("""**Mapeamento da 915** """)
    
    tabela915 = pd.DataFrame({

                    " Nome ": [
                    "NF-E",
                    "CHAVE DANFE",
                    "XML",
                    "NR1/NR2",
                    "CTR"
                ],

                "Descrição": [
                    "Número da Nota Fiscal.",
                    "Chave pode ser copiada com Ctrl-V e colada com Ctrl-C na opção 004 para gerar o CT-e correspondente.",
                    "O S indica que o XML da DANFE está disponível, o que facilita a geração do CT-e.",
                    "Etiquetas sequenciais dos volumes coletados utilizadas para descarregamento com SSWBar.",
                    "S indica que no momento da geração do relatório o pré-CTRC já se encontra emitido."
                ],

            })
    st.dataframe(
                    tabela915,
                    use_container_width=True,
                    hide_index=True
                )
    components.html("""
        <div class="mermaid">
        erDiagram

            206{
                int id PK
                string Veiculo
                numeric Motorista
                time Hora
                int Coleta
                string CNPJ Remetente
                text Remetente
                int NF-E 
                string Chave Danfe
                text XML 
                text NR1
                text NR2
                text CTR
                
            }

            915 {
                int id PK
                string sigla_ctrc
                string numero_ctrc
                date coluna_3
               sigla_cte	 
              numero_cte	
                     ctrc/subcontr	 nro_chave_acesso_cte	 situacao_ctrc	 data_emissao	 hora_emissao	 prev_ent	 fil_dest	 praca_destino	 cidade_destino	 uf_destino	 qtde_volume	 tipo_mercadoria	 veiculo_coleta	 veiculo_entrega	 cubagem_m3	 kg_real	 kg_calculo	 valor_n_fiscal	 tipo_frete	 sit_liquidacao	 numero_controle	 usu_inc	 remetente_nome	 remetente_cnpj	 remetente_inscr	 remet_endereco	 remet_cep	 remet_cidade	 remet_uf	 remet_data_inc	 destinatario_nome	 dest_cnpj	 dest_inscr	 dest_endereco	 dest_cep	 dest_cidade	 dest_uf	 dest_data_inc	 pagador_nome	 pag_cnpj	 pag_inscr	 pag_endereco	 pag_cep	 pag_cidade	 pag_uf	 pag_data_inc	 unid_resp_pagador	 observ1	 observ2	 entrega/redesp_nome	 entr_endereco	 entr_cep	 entr_cidade	 entr_uf	 ult_ocorr_local	 ult_ocorr_data	 ult_ocorr_hora	 ult_ocorr_codigo	 ult_ocorr_descricao	 ult_instr	 distancia_km	 tarifa	 tabela_calculo	 desc_tabela	 frete_peso	 frete_valor	 aliquota	 vlr_icms	vlr_imposto_cli	despacho	 cat	itr	 gris	coleta	 tde	trt	 canhoto	pedagio	 outros_impostos	desconto	 suframa	tda	 valor_tas	reembolso	 valor_pos	valor_frete	cfop	 tipo_cobranca	fatura	 valor_liquido	vlr_liquidado	 data_liquidacao	data_credito_caixa	 rel_comissao_exp	rel_comissao rec	 rel_comissao_vend	pacote	 sgl_unid_emit	nro_manifesto	 cod_vendedor	nome_vendedor	 tipo_documento	entrega_dificil	adicional_frete	vlr_comissao_rec	vlr_comissao_exp	tar	data_autorizacao	hora_autorizacao	vlr_agendamento

            }

            %% Relacionamento futuro
            %% TABELA_1 ||--o{ TABELA_2 : chave_a_definir

        </div>

        <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';

        mermaid.initialize({
            startOnLoad: true,
            theme: 'default',
            securityLevel: 'loose'
        });
        </script>
        """, height=500)
    with abas[1]:
        #st.header("Titulo Grandão")

        st.markdown("""
                            <h5>Power Query:</h5>""", unsafe_allow_html=True)
        st.markdown("""
            <style>
                .query-card {
                    border: 1px solid #d9e2ec;
                    border-radius: 8px;
                    padding: 22px 24px;
                    background: #ffffff;
                    box-shadow: 0 1px 3px rgba(15, 23, 42, 0.08);
                    margin-bottom: 18px;
                }

                .query-card h3 {
                    margin: 0 0 8px 0;
                    color: #0f172a;
                    font-size: 1.25rem;
                    font-weight: 700;
                }

                .query-card p {
                    margin: 0;
                    color: #475569;
                    line-height: 1.55;
                }

                .query-grid {
                    display: grid;
                    grid-template-columns: repeat(2, minmax(0, 1fr));
                    gap: 14px;
                    margin-top: 16px;
                }

                .query-step {
                    border: 1px solid #e5e7eb;
                    border-radius: 8px;
                    padding: 16px;
                    background: #f8fafc;
                }

                .query-step strong {
                    display: block;
                    margin-bottom: 8px;
                    color: #1e293b;
                    font-size: 0.98rem;
                }

                .query-step ul {
                    margin: 8px 0 0 18px;
                    padding: 0;
                    color: #475569;
                    line-height: 1.55;
                }

                .query-tag {
                    display: inline-block;
                    margin: 4px 4px 0 0;
                    padding: 4px 8px;
                    border-radius: 6px;
                    background: #e0f2fe;
                    color: #075985;
                    font-size: 0.82rem;
                    font-weight: 600;
                }

                .query-note {
                    border-left: 4px solid #2563eb;
                    padding: 12px 14px;
                    margin-top: 16px;
                    background: #eff6ff;
                    color: #334155;
                    border-radius: 0 8px 8px 0;
                }

                @media (max-width: 900px) {
                    .query-grid {
                        grid-template-columns: 1fr;
                    }
                }
            </style>

            <div class="query-card">
                <h3>Transformações Aplicadas na Consulta</h3>
                <p>
                    A extração dos dados é realizada a partir do banco PostgreSQL,
                    utilizando conexão ODBC com o ambiente corporativo da Carvalima.
                    A origem da consulta é a view <strong>vw_206</strong>, localizada
                    no schema <strong>public</strong>.
                </p>

                <div class="query-grid">
                    <div class="query-step">
                        <strong>1. Filtro e padronização inicial</strong>
                        <p>
                            Os registros são filtrados por <span class="query-tag">RangeStart</span>
                            e <span class="query-tag">RangeEnd</span>. Depois, a coluna
                            <span class="query-tag">Data Arquivo</span> é convertida para data,
                            garantindo consistência para análises temporais no Power BI.
                        </p>
                    </div>

                    <div class="query-step">
                        <strong>2. Chave de integração</strong>
                        <p>
                            São criadas cópias das colunas <span class="query-tag">CHAVE DANFE</span>
                            e <span class="query-tag">NF-E</span> para formar a chave
                            <span class="query-tag">id_danfe_nfe</span>, usada no relacionamento
                            entre as views 206 e 915.
                        </p>
                    </div>

                    <div class="query-step">
                        <strong>3. Enriquecimento com a view 915</strong>
                        <p>
                            É realizado um <strong>Left Join</strong> com a
                            <span class="query-tag">view_915</span>, relacionando
                            <span class="query-tag">id_danfe_nfe</span> com
                            <span class="query-tag">id_chave_nota_fiscal</span>.
                        </p>
                        <ul>
                            <li>CTRC emitido</li>
                            <li>Data e hora de emissão</li>
                            <li>Chave de acesso da NF-e</li>
                        </ul>
                    </div>

                    <div class="query-step">
                        <strong>4. Classificação por horário</strong>
                        <p>
                            A coluna de hora de emissão é tratada para criar
                            <span class="query-tag">grupo_hora_emissao</span>, separando
                            as emissões por faixa horária.
                        </p>
                        <ul>
                            <li>Menor que 19hs</li>
                            <li>Maior que 19hs</li>
                            <li>Vazio</li>
                        </ul>
                    </div>

                    <div class="query-step">
                        <strong>5. Padronização da chave DANFE</strong>
                        <p>
                            A coluna <span class="query-tag">chave_danfe_2</span> recebe os
                            primeiros 44 caracteres da chave DANFE, facilitando validações
                            e cruzamentos futuros.
                        </p>
                    </div>

                    <div class="query-step">
                        <strong>6. Chave técnica operacional</strong>
                        <p>
                            A chave <span class="query-tag">id_ctrc_busca</span> identifica
                            cada ocorrência operacional a partir da concatenação dos campos:
                        </p>
                        <ul>
                            <li>CHAVE DANFE</li>
                            <li>NR1</li>
                            <li>NR2</li>
                            <li>COLETA</li>
                            <li>HORA</li>
                        </ul>
                    </div>
                </div>

                <div class="query-note">
                    Essa estrutura apoia validações, rastreabilidade e análises de
                    consistência dos dados dentro do modelo.
                </div>
            </div>
            """, unsafe_allow_html=True)
