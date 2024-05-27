import streamlit as st
import pandas as pd
import json
from codes.render_table import draw_table
from codes.auth_user import handle_authentication
from src.style_header import css_style,hidden_menu
from codes.funcs import add_img_app
# Chama a função para manipular a autenticação
user_info = handle_authentication()
st.set_page_config(layout="wide")
add_img_app('src/img_fundo.jpg')
st.markdown(hidden_menu, unsafe_allow_html=True)
# Carrega os dados do arquivo JSON
try:
    with open('files/data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    df = pd.DataFrame(data)
except FileNotFoundError:
    st.error("Arquivo 'data.json' não encontrado. Por favor, crie o arquivo antes de executar o programa.")
    st.stop()

# Verifica se o usuário está autenticado
if user_info:
    st.markdown("<h1 class='title'>Agendamentos de Laboratórios</h1>", unsafe_allow_html=True)
    st.markdown(f"<h3 class='user_name'>Olá Professor: {user_info['name']}</h3>", unsafe_allow_html=True)
    editable = True

# Render CSS styles
    st.markdown(css_style, unsafe_allow_html=True)
#st.markdown("<div class='success-message'>Você está logado.</div>", unsafe_allow_html=True)
    turno = st.selectbox("Selecione o turno:", ["Matutino", "Vespertino", "Noturno"], key='select-box')
    #if turno == 'Vespertino':
        #st.markdown("<iframe src='http://192.168.0.106:8502' width='100%' height='500'></iframe>", unsafe_allow_html=True)
    #st.markdown(f"<div class='select-box'>Você selecionou o turno: {turno}</div>", unsafe_allow_html=True)
    # Aplicar o estilo da tabela com Bootstrap
    draw_table(df, table_height=480, editable=editable, save_url='http://127.0.0.1:5000/save_data')
