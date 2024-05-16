import base64
import json

import streamlit as st
from src.styles_css import custom_css, custom_main, hidden_menu

from codes.funcs import add_bg_from_local, add_bg_from_body
from codes.files import json_data, links
from test import css

from codes.funcs import add_bg_from_local, add_img_app
from codes.files import json_string, links

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
st.markdown('<h1 class="h1-title">Check List de itens</h1></div>', unsafe_allow_html=True)

# Usar o estilo personalizado dentro de um contêiner
data_dict = json.loads(json_string)
with st.container() as container:
    with open("codes/output.json", "r") as json_file:
        data = json.load(json_file)

        # Itera sobre os dados e faz o que precisar

    labs = list(data.keys())
    # Menu selecionável
    lab_selecionado = st.selectbox('Selecione um laboratório:', labs)

    # Exibir resultado com base no laboratório selecionado
    if lab_selecionado:
        lab_info = data[lab_selecionado]
        #st.write(f'Nome do Laboratório: {lab_info["nome"]}')
        #st.write(f'Número de Máquinas: {lab_info["N_maquinas"]}')
        #st.write('Softwares Instalados:')


        st.markdown('<div class="custom-container"> ',unsafe_allow_html=True)
        st.markdown("<div class='custom-div'>Conteúdo da div 1</div>", unsafe_allow_html=True)
        st.markdown("<div class='custom-div'>Conteúdo da div 2</div>", unsafe_allow_html=True)
        st.markdown("<div class='custom-div'>Conteúdo da div 3</div>", unsafe_allow_html=True)
        st.markdown("<div class='custom-div'>Conteúdo da div 4</div>", unsafe_allow_html=True)


        add_bg_from_local('src/senai-web.jpg')

        custom = "<div class='container-main'>"
        custom += f'<h3>{lab_selecionado}</h3>'
        custom += f'<h5> ✅ Nº de maquinas: {lab_info["N_maquinas"]}</h5>'
        custom += f'<h5> ❗ Nº Nao funciona: {lab_info["N_maquinas"]}</h5>'
        custom += f'<h5> ✅ Softwares disponiveis:</h5>'

        for software in lab_info["softweres_instalados"]:

            custom += f'<ul>'
            custom += f'<li> 🆗 {software}</li>'
            custom += f'</ul>'

        custom += "</div>"
        st.markdown(custom, unsafe_allow_html=True)


# Carregar o estilo CSS personalizado para a parte principal da página
st.markdown(custom_main, unsafe_allow_html=True)
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
add_bg_from_body('src/senai-web.jpg')