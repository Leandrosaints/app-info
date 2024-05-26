import streamlit as st
import pandas as pd
import json
from codes.render_table import draw_table
from codes.auth_user import handle_authentication
from src.style_header import css_style, hidden_menu
from codes.funcs import add_img_app# Chama a função para manipular a autenticação
user_info = handle_authentication()

if st.session_state.get('is_authenticated', False):
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

    st.markdown("<h1 class='title'>Agendamentos de Laboratórios</h1>", unsafe_allow_html=True)
    st.markdown(f"<h3 class='user_name'>Olá Professor: {user_info['name']}</h3>", unsafe_allow_html=True)
    editable = True

    # Render CSS styles
    st.markdown(css_style, unsafe_allow_html=True)

    turno = st.selectbox("Selecione o turno:", ["Matutino", "Vespertino", "Noturno"], key='select-box')

    # Aplicar o estilo da tabela com Bootstrap
    draw_table(df, table_height=480, editable=editable, save_url='http://127.0.0.1:8000/save_data')
else:
    st.write("Você precisa estar autenticado para acessar esta página.")
