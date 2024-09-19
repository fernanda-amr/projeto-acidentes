import streamlit as st
st.title("Dados do usuario")
st.dataframe(st.session_state["dados"])