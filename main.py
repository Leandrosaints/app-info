import base64
import streamlit as st
from src.styles_css import custom_css, custom_main, hidden_menu

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

def add_img_app(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover;
        background-position: center bottom;
        background-repeat: no-repeat;
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
    "Quadro branco disponível",
]

links = [
    {"text": "home", "url": "https://example.com/1", "icon": "fa-sharp fa-solid fa-house"},
    {"text": "form", "url": "https://example.com/2","icon": "fa-solid fa-list-check"},
    {"text": "contact", "url": "https://example.com/3","icon": "fa-solid fa-mobile" }
]


Ambiente = 'laboratorio'

def generate_links(links):
    links_html = "<div class='st-emotion-cache-18ni7ap'>"
    links_html += """<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">"""
    links_html += "<div class='link-container'>"
    for link in links:
        links_html += "<div class='link-item'>"
        if "icon" in link:
            links_html += f"<a href='{link['url']}'><i class='{link['icon']}'></i></a>"
        links_html += f"<a href='{link['url']}'>{link['text']}</a>"
        links_html += "</div>"
    links_html += "</div>"
    links_html += "</div>"
    return st.markdown(links_html, unsafe_allow_html=True)


# Adicione os links à página usando st.markdown
generate_links(links)

# Carregar o arquivo CSS personalizado
st.markdown(hidden_menu, unsafe_allow_html=True)
st.markdown(custom_css, unsafe_allow_html=True)

# Usar o estilo personalizado dentro de um contêiner
with st.container() as container:
    st.markdown('<div class="custom-container"> '
                f'<h1>Check List de itens em {Ambiente}</h1>', unsafe_allow_html=True)

    add_bg_from_local('src/senai-web.jpg')
    #add_img_app('src/img.jpg')

    custom = "<div class='container-main'>"
    for item in classroom_items:
        custom += f'<h5> ✅ {item}</h5>'
    custom += "</div>"
    st.markdown(custom, unsafe_allow_html=True)

# Carregar o estilo CSS personalizado para a parte principal da página
st.markdown(custom_main, unsafe_allow_html=True)
