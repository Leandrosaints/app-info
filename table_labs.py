import streamlit as st
import pandas as pd
import json
from codes.render_table import draw_table
from auth_user import handle_authentication
from style_header import css_style
from codes.funcs import add_img_app
# Chama a função para manipular a autenticação
user_info = handle_authentication()
st.set_page_config(layout="wide")
add_img_app('src/img_fundo.jpg')
# Carrega os dados do arquivo JSON
try:
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    df = pd.DataFrame(data)
except FileNotFoundError:
    st.error("Arquivo 'data.json' não encontrado. Por favor, crie o arquivo antes de executar o programa.")
    st.stop()

# Verifica se o usuário está autenticado
if user_info:
    st.markdown("<div class='title'>Agendamentos de Laboratórios</div>", unsafe_allow_html=True)

    st.markdown(f"<h4 class='user_name'>Olá Professor: {user_info['name']}</h4>", unsafe_allow_html=True)
    editable = True

# Render CSS styles
    st.markdown(css_style, unsafe_allow_html=True)
#st.markdown("<div class='success-message'>Você está logado.</div>", unsafe_allow_html=True)

    turno = st.selectbox("Selecione o turno:", ["Matutino", "Vespertino", "Noturno"], key='select-box')
    #st.markdown(f"<div class='select-box'>Você selecionou o turno: {turno}</div>", unsafe_allow_html=True)
    # Aplicar o estilo da tabela com Bootstrap
    draw_table(df, table_height=480, editable=editable, save_url='http://127.0.0.1:8000/save_data')
