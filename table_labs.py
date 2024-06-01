import streamlit as st
import pandas as pd
import json
from codes.render_table import draw_table
from codes.auth_user import handle_authentication
from src.style_header import css_style,hidden_menu
from codes.funcs import add_img_app
# Chama a função para manipular a autenticação
#user_info = handle_authentication()
st.set_page_config(layout="wide")
add_img_app('src/img_fundo.jpg')
st.markdown(hidden_menu, unsafe_allow_html=True)
text = """
    Olá! Bem-vindo ao Sistema Básico de Agendamentos de labs.
    Esta é uma versão beta, então por favor, tenha paciência, Obrigado 🫡!
"""
st.markdown("<h1 class='title'>Agendamentos de Laboratórios</h1>", unsafe_allow_html=True)
st.markdown(f"<h2 class='user_name'>{text}</h2>", unsafe_allow_html=True)
editable = True


st.markdown(css_style, unsafe_allow_html=True)
turno = st.selectbox("Selecione o turno:", ["Matutino", "Vespertino"], key='select-box')

draw_table(table_height=480, editable=editable, save_url=f'https://app-info.onrender.com/write_data/{turno}', turno=turno)
