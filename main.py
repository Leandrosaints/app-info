import base64
import streamlit as st
from src.styles_css import custom_css, custom_main, custom_menu
from streamlit_option_menu import option_menu
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
    <style>
    .custom-container {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover;
        background-position: center bottom;
        background-repeat: no-repeat;
        position: relative;
         margin-top: 0px; /* Reduz a margem superior */
       
    }}
    
    </style>
    """,
        unsafe_allow_html=True
    )

# Definir o layout da página
st.set_page_config(layout="wide", initial_sidebar_state='auto')

# Lista de itens da sala de aula
classroom_items = [
    "Projetor funcionando",
    "Ar condicionado funcionando",
    "Computador funcionando",
    "Iluminação adequada",
    "Quadro branco disponível"
]

Ambiente = 'laboratorio'

# Carregar o arquivo CSS personalizado
st.markdown(custom_css, unsafe_allow_html=True)



# Usar o estilo personalizado dentro de um contêiner
with st.container() as container:



    selected = option_menu(
        menu_title=None,
        options=["Home", "Upload", "Analytics", 'Settings', 'Contact'],
        icons=['house', 'cloud-upload', "graph-up-arrow", 'gear', 'phone'],
        menu_icon="cast",
        orientation='horizontal',
        styles=custom_menu
    )

    st.markdown('<div class="custom-container"> '
                f'<h1>Check List de itens em {Ambiente}</h1>',unsafe_allow_html=True)
    add_bg_from_local('src/senai-web.jpg')


    custom = "<div class='container-main'>"
    for item in classroom_items:
        custom += f'<h5> ✅ {item}</h5>'
    custom += "</div>"
    st.markdown(custom, unsafe_allow_html=True)

st.markdown(custom_main, unsafe_allow_html=True)

