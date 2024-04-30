import streamlit as st
import base64

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
        height: auto;
        background-position: center bottom;
        opacity: 0.5; 
        background-repeat: no-repeat; 
        margin: 0 auto; 
        background-color: rgba(255, 255, 255, 0.5);      
       
       
    }}
    </style>
    """,
        unsafe_allow_html=True
    )

# Definir o layout da página
st.set_page_config(layout="wide", initial_sidebar_state='expanded')

# Lista de itens da sala de aula
classroom_items = [
    "Projetor funcionando",
    "Ar condicionado funcionando",
    "Computador funcionando",
    "Iluminação adequada",
    "Quadro branco disponível"
]
Ambiente = 'laboratorio'

# Criar o título da página
st.title(f"Check List de itens em {Ambiente}")

# Carregar o arquivo CSS personalizado
with open('src/styles.css') as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Criar o contêiner principal
container_main = st.container()
with container_main:

    for item in classroom_items:
        st.write(f"✅ {item}")

add_bg_from_local('src/senai-web.jpg')