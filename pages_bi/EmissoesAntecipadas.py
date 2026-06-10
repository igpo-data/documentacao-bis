import streamlit as st
import pandas as pd
import streamlit.components.v1 as components


def render():
    st.title("Emissões Antecipadas")

    st.info("""
    Este BI tem pos finalidade o calculo dados aos motorista. 
            \n 
            Base: 915 e 206. 
    """)

    abas = st.tabs([
        "Modo de Extração",
        "BI"
    ])
    
    with abas[0]:
        st.markdown("""
                            <h5>Modo de extração</h5>""", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)

        with col1:
                st.image("img/Tela206.PNG", caption="Tela de Extração da 206", use_container_width=True)

        with col2:
            st.image("img/Tela915.PNG", caption="Tela de Extração da 915 ", use_container_width=True)
        
        st.markdown("""**Obs**: A tela de extração da 915 muda momentaneamente, sendo o formato de tela como o da imagem, contendo a opção tipo de dados: CTRC E Fatura. 
                            """)

        st.markdown("""
                            <h5>Dados Brutos.</h5>""", unsafe_allow_html=True)
        
       ########### tabela de exemplo 
        tabela = pd.DataFrame({

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
                    tabela,
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
                string coluna_1
                numeric coluna_2
                date coluna_3
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
                            <h4>Visual:</h4>""", unsafe_allow_html=True)