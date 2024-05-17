import base64
import json

import streamlit as st
from src.styles_css import custom_css, custom_main, hidden_menu

from codes.funcs import add_bg_from_local, add_bg_from_body

from test import css

from codes.funcs import add_bg_from_local, add_img_app
from codes.files import links_forms,links
from search import search_bar

# Definir o layout da página
st.set_page_config(layout="wide", initial_sidebar_state='auto')
#ad_img_app('src/fundo.jpg')

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


# Iterar sobre as chaves e valores do dicionário

# Carregar o arquivo CSS personalizado
st.markdown(hidden_menu, unsafe_allow_html=True)
st.markdown(custom_css, unsafe_allow_html=True)
st.markdown('<h1 class="h1-title">Levantamentos de Laboratórios</h1>', unsafe_allow_html=True)

# Usar o estilo personalizado dentro de um contêiner

with (st.container() as container):

    custom = "<div class='container-main'>"


    add_img_app('src/37256872-network-background.jpg')

    for link in links_forms:

        custom += f"<a href='{link['url']}'>✅ {link['text']}</a>"

    custom += "</div>"
    st.markdown(custom, unsafe_allow_html=True)


# Carregar o estilo CSS personalizado para a parte principal da página
st.markdown(custom_main, unsafe_allow_html=True)
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
add_bg_from_body('src/senai-web.jpg')