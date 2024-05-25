import streamlit as st
import pandas as pd
import json
from codes.render_table import draw_table
from auth_user import handle_authentication

# Chama a função para manipular a autenticação
user_info = handle_authentication()
st.set_page_config(layout="wide")

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
    st.write(f"Olá, {user_info['name']} ({user_info['email']})!")
    st.success("Você está logado.")
    editable = True

st.title("Agendamentos de Laboratórios")
turno = st.selectbox("Selecione o turno:", ["Matutino", "Vespertino", "Noturno"])
st.write(f"Você selecionou o turno: {turno}")

# Aplicar o estilo da tabela com Bootstrap
draw_table(df, table_height=400, editable=editable, save_url='http://127.0.0.1:8000/save_data')
