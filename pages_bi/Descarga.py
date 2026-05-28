import streamlit as st
import pandas as pd
import streamlit.components.v1 as components


def render():
    st.title("Descarga")

    st.info("""
   Esse BI tem por finalidade apresenta o tempo de descarga 
   e classificação da meta por unidade. 
    """)

    abas = st.tabs([
        "Regras de Negócio",
        "Detalhamento Descargas - Emissão",
        "Detalhamento Descargas - Início"
    ])

    with abas[0]:

        st.markdown("""
                    <h4>Regra da Descarga</h4>""", unsafe_allow_html=True)

        
        st.markdown("""
      A regra mede o intervalo entre o início e o fim da descarga, em segundos, e depois 
    compara esse tempo com o limite permitido para cada unidade emissora ou combinação específica
    de unidade destino + unidade emissora.  
                 """)
       
        st.markdown("""
                    <h5>Campos utilizados na regra</h5>""", unsafe_allow_html=True)
        
       ########### tabela de exemplo 
        tabela1 = pd.DataFrame({

                "Campo": [
                   "dat_DataInicioDescarga",
                   "dat_HoraInicioDescarga",
                   "datDataFimDescarga",
                   "dat_HoraFimDescarga",
                   "tempo_DescargaSegundos",
                   "f.nom_UnidadeEmissora",
                   "f.nom_UnidadeDestino",
                   "id_PeriodoEmissao"],

                "Descrição": [
                    "Data de início da descarga",
                    "Hora de início da descarga",
                    "Data de fim da descarga",
                    "Hora de fim da descarga",
                    "Tempo calculado entre início e fim da descarga, ja com os possiveis descontos ",
                    "Unidade emissora usada para definir a meta de tempo.",
                    "Unidade destino usada em exceções específicas para CGR.",
                    "Período de emissão usado na exceção da unidade EDO até 31/03/2024."]
                })
        st.dataframe(
                    tabela1,
                    use_container_width=False,
                    hide_index=True
                )
        
        st.markdown("""
                <h5>Regra de cálculo do tempo de descarga</h5>""", unsafe_allow_html=True)
        
        st.markdown(""" Pimeiro, o processo valida se existe data de ínicio e data de fim de descarga.
                    Quando umas dessas datas está vazia, o tempo calculado recebe NULL. 
                    Quando as datas existem, o cálculo monta dois timestamps: um com a data/hora de ínicio e outro 
                    com a data/hora de fim. A diferença entre eles é calculada em segundos por TIMESTAMPDIFF. 
                            """)
        st.markdown("""
                <h5>Descontos aplicados por faixa de horário</h5>""", unsafe_allow_html=True)
        
        st.markdown(""" Existem duas janelas de horário em que o tempo bruto da descarga recebe desconto automático:""")

        tabela2 = pd.DataFrame({
                "Condição do início da descarga": [
                   "Início entre 10:00:00 e 10:59:59 ",
                   "Início entre 02:00:00 e 03:29:59 ",
                   "Demais horários"
                   ],

                "Desconto": [
                    "Desconta 7.200 segundos",
                    "Desconta 5.400 segundos",
                    "Não há desconto"
                    ], 

                "Interpretação": [
                    "Equivale a descontar 2 horas do tempo total",
                    "Equivale a descontar 1 hora e 30 minutos do tempo total",
                    "O tempo calculado é a diferença direta entre fim e início."
                    ] })
        
        st.dataframe(
                    tabela2,
                    use_container_width=False,
                    hide_index=True
                )
        st.markdown("""**Observação importante:** a regra considera apenas o horário de 
        início da descarga para aplicar o desconto. O horário de fim não interfere na
        escolha do desconto, apenas no cálculo do intervalo total. """)

        st.markdown(""" <h5>Regra de classificação da meta</h5>""", unsafe_allow_html=True)

        st.markdown("""Após calcular o tempo em segundos, a regra compara *tempo_DescargaSegundos* com o limite definido para a
            unidade. Se o tempo estiver dentro do limite, o resultado é Dentro da Meta. Caso contrário, é Fora da Meta.
            Quando *tempo_DescargaSegundos* está nulo, a classificação final é Fora da Meta, porque não existe tempo
            válido para comprovar cumprimento da meta.
                """)
        
        st.markdown(""" <h5>Tabela de unidades e tempo de descarga permitido</h5>""", unsafe_allow_html=True)
        
        tabela3 = pd.DataFrame({
                "Unidade/Condição": [
                   "CQP, JD1, SOD, ROO, SIN, ARA,TRL ",
                   "BSB",
                   "EDO até 31/03/2024",
                   "CGB, CGR, CVL, CWB, FLN, JIP, JUD, JVE, LDB, MGA, MII, NGT, POA, PVH, SAO, SER, XAP, VHA",
                   "GOA, RBP",
                   "Destino CGR + Emissora AVO ou NAT",
                   "Destino CGR + Emissora DRD ou TRL",
                   "Demais unidades não listadas"
                   ],

                "Base da Regra": [
                    "Unidade Emissora",
                    "Unidade Emissora",
                    "Unidade Emissora + Período",
                    "Unidade Emissora",
                    "Unidade Emissora",
                    "Exceção destino/emissora",
                    "Exceção destino/emissora",
                    "Regra padrão"
                    ], 

                "Metas em horas": [
                    "2 horas",
                    "3 horas",
                    "3 horas",
                    "5 horas",
                    "6 horas",
                    "3 horas",
                    "2 horas",
                    "1 hora"
                    ] })
        
        st.dataframe(
                    tabela3,
                    use_container_width=False,
                    hide_index=True
                )

        st.markdown(""" <h5>Ordem de prioridade das regras</h5>""", unsafe_allow_html=True)

        st.markdown("""1. Se o tempo calculado for NULL, a descarga é classificada como Fora da Meta.\n
2. A regra verifica primeiro os grupos de unidades emissoras com metas específicas.\n
3. Depois avalia as exceções de destino CGR combinadas com emissoras específicas.\n
4. Se nenhuma condição anterior for atendida, aplica a regra padrão de 1 hora.\n
5. Se o tempo ultrapassar o limite da condição aplicável, o resultado final é Fora da Meta.
                """)
        
        st.markdown(""" <h5>Pontos de atenção</h5>""", unsafe_allow_html=True)

        st.markdown("""O limite sempre há de ser com 1 segundo a mais que a hora cheia. 
                    Exemplo: 2 horas seriam 7.200 segundos,mas usar <= 7.201.\n
A unidade TRL aparece em duas regras: como emissora com meta de 2 horas e também na exceção
destino CGR + emissora TRL com meta de 2 horas. Na prática, permanece 2 horas.\n
A unidade EDO só entra na meta de 3 horas quando id_PeriodoEmissao <= 20240331. Após esse período,
se não houver outra regra, ela cai na regra padrão de 1 hora.
Os descontos de horário podem reduzir o tempo final. Caso o desconto seja maior que o intervalo bruto,
o resultado pode ficar negativo, dependendo dos dados de entrada.
A montagem dos timestamps usa hora e minuto, descartando os segundos originais no cálculo do
intervalo
                """)


