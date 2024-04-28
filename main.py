import streamlit as st

# Definir o layout da página
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")


# Lista de itens da sala de aula
classroom_items = [
    "Projetor funcionando",
    "Ar condicionado funcionando",
    "Computador funcionando",
    "Iluminação adequada",
    "Quadro branco disponível"
]
Ambiente = 'laboratorio'
# Criar o card com bordas arredondadas

st.markdown(f"""
<div style="border-radius: 10px; padding: 20px;">
    <h2 style="color: #333;">Check List de itens em {Ambiente} </h2>
    
""", unsafe_allow_html=True)

# Exibir a lista de itens dentro do card
for item in classroom_items:
    st.markdown(f"✅ {item}</div>", unsafe_allow_html=True)

