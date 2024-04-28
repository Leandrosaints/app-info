import streamlit as st

# Definir o layout da página
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# Título da página
st.title("Sala de Aula")

# Lista de itens da sala de aula
classroom_items = [
    "Projetor funcionando",
    "Ar condicionado funcionando",
    "Computador funcionando",
    "Iluminação adequada",
    "Quadro branco disponível"
]

# Criar o card com bordas arredondadas
st.markdown("""
<div style="background-color: white; border-radius: 10px; padding: 20px;">
    <h2 style="color: #333;">Itens da Sala de Aula</h2>
    <ul style="color: #333; font-size: 1.2rem;">
""", unsafe_allow_html=True)

# Exibir a lista de itens dentro do card
for item in classroom_items:
    st.markdown(f"    <li style='margin-bottom: 10px;'>✅ {item}</li>", unsafe_allow_html=True)

st.markdown("""
    </ul>
</div>
""", unsafe_allow_html=True)

# Ajustar o estilo da página
st.markdown("""
<style>
    .stApp {
        background-color: #f0f0f0;
        padding: 2rem;
    }
</style>
""", unsafe_allow_html=True)
