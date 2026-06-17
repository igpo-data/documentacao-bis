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

        st.markdown("**Mapeamento das colunas da consulta**")
        tabela_power_query = pd.DataFrame({
            "Coluna": [
                "Data Arquivo",
                "CHAVE DANFE - Copiar",
                "NF-E - Copiar",
                "id_danfe_nfe",
                "915.ctrc",
                "915.data_emissao",
                "915.hora_emissao",
                "915.nro_chave_acesso_nfe",
                "hora_emissao",
                "grupo_hora_emissao",
                "chave_danfe_2",
                "id_ctrc_busca",
            ],
            "Descrição": [
                "Data do arquivo processado. Utilizada para aplicação do filtro incremental através dos parâmetros RangeStart e RangeEnd.",
                "Cópia da coluna CHAVE DANFE criada para permitir a construção de chaves auxiliares sem alterar o campo original.",
                "Cópia da coluna NF-E utilizada na composição da chave de relacionamento com a base 915.",
                "Chave composta pela concatenação da CHAVE DANFE e da NF-E. Utilizada para relacionar os registros da vw_206 com a view_915.",
                "Número do CTRC retornado da view_915 após o relacionamento entre as tabelas.",
                "Data de emissão do CTRC obtida na view_915.",
                "Horário de emissão do CTRC obtido na view_915.",
                "Chave de acesso da Nota Fiscal Eletrônica retornada pela view_915.",
                "Campo derivado do horário de emissão, utilizado para análises e classificações por horário.",
                "Classificação do horário de emissão em faixas de horário para análise operacional.",
                "Campo contendo os primeiros 44 caracteres da chave DANFE. Utilizado para padronização e validações.",
                "Chave técnica criada pela concatenação da CHAVE DANFE, NR1, NR2, COLETA e HORA. Utilizada para identificação única e rastreabilidade dos registros.",
            ],
        })
        st.dataframe(tabela_power_query, use_container_width=True, hide_index=True)

        col_regras, col_chave = st.columns(2)

        with col_regras:
            st.markdown("**Detalhamento do campo `grupo_hora_emissao`**")
            tabela_grupo_hora = pd.DataFrame({
                "Valor": [
                    "Menor que 19hs",
                    "Maior que 19hs",
                    "Vazio",
                ],
                "Regra": [
                    "Horário de emissão menor ou igual ao horário limite definido para antecipação.",
                    "Horário de emissão superior ao horário limite definido para antecipação.",
                    "Registro sem horário de emissão informado.",
                ],
            })
            st.dataframe(tabela_grupo_hora, use_container_width=True, hide_index=True)

        with col_chave:
            st.markdown("**Detalhamento do campo `id_ctrc_busca`**")
            tabela_id_ctrc = pd.DataFrame({
                "Campo utilizado": [
                    "CHAVE DANFE",
                    "NR1",
                    "NR2",
                    "COLETA",
                    "HORA",
                ],
                "Finalidade": [
                    "Identificação da NF-e",
                    "Número de referência operacional",
                    "Número complementar de referência",
                    "Identificador da coleta",
                    "Horário do registro operacional",
                ],
            })
            st.dataframe(tabela_id_ctrc, use_container_width=True, hide_index=True)

        with st.container(border=True):
            st.markdown("""
            A extração dos dados é realizada a partir do banco PostgreSQL,
            utilizando conexão ODBC com o ambiente corporativo da Carvalima.
            A origem da consulta é a view **vw_206**, localizada no schema **public**.
            """)

            col1, col2 = st.columns(2)

            with col1:
                with st.container(border=True):
                    st.markdown("**1. Filtro e padronização inicial**")
                    st.markdown("""
                    Os registros são filtrados por `RangeStart` e `RangeEnd`.
                    Depois, a coluna `Data Arquivo` é convertida para data,
                    garantindo consistência para análises temporais.
                    """)

                with st.container(border=True):
                    st.markdown("**3. Enriquecimento com a view 915**")
                    st.markdown("""
                    É realizado um **Left Join** com a `view_915`, relacionando
                    `id_danfe_nfe` com `id_chave_nota_fiscal`.

                    Informações incorporadas:

                    - CTRC emitido
                    - Data e hora de emissão
                    - Chave de acesso da NF-e
                    """)

                with st.container(border=True):
                    st.markdown("**5. Padronização da chave DANFE**")
                    st.markdown("""
                    A coluna `chave_danfe_2` recebe os primeiros 44 caracteres da
                    chave DANFE, facilitando validações e cruzamentos futuros.
                    """)

            with col2:
                with st.container(border=True):
                    st.markdown("**2. Chave de integração**")
                    st.markdown("""
                    São criadas cópias das colunas `CHAVE DANFE` e `NF-E` para
                    formar a chave `id_danfe_nfe`, usada no relacionamento entre
                    as views 206 e 915.
                    """)

                with st.container(border=True):
                    st.markdown("**4. Classificação por horário**")
                    st.markdown("""
                    A coluna de hora de emissão é tratada para criar
                    `grupo_hora_emissao`, separando as emissões por faixa horária.

                    Classificações:

                    - Menor que 19hs
                    - Maior que 19hs
                    - Vazio
                    """)

                with st.container(border=True):
                    st.markdown("**6. Chave técnica operacional**")
                    st.markdown("""
                    A chave `id_ctrc_busca` identifica cada ocorrência operacional
                    a partir da concatenação dos campos:

                    - CHAVE DANFE
                    - NR1
                    - NR2
                    - COLETA
                    - HORA
                    """)

            st.info(
                "Essa estrutura apoia validações, rastreabilidade e análises de "
                "consistência dos dados dentro do modelo."
            )
