import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Meu sistema Streamlit",
    page_icon="book",
    layout="wide" #ocupa toda a tela e centered o centro
)

lateral = st.sidebar
data = lateral.date_input("Selecione a data")
cidade = lateral.selectbox("Selecione a cidade", ["Belo Horizonte", "Rio de Janeiro", "São Paulo"])

@st.cache_data
def carregar_dados():
    dados = pd.read_csv("acidentes.csv")
    return dados

dados = carregar_dados()

st.session_state["dados"] = dados
st.session_state["data"] = data
st.session_state["cidade"] = cidade

st.title("Dados")

col1, col2 = st.columns(2)
tabela = col1.dataframe(dados)
municipios = dados["municipio"].value_counts()
col2.bar_chart(municipios)

st.subheader("Cidade")
st.write(f"A cidade selecionada foi {cidade}")
