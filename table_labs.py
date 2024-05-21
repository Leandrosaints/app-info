import streamlit as st
import pandas as pd

# Inicializando o DataFrame 5x5
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame({
        'Seg': ['João', 'Maria', 'Pedro', 'Ana', 'Lucas'],
        'Ter': ['Fernanda', 'Rafael', 'Beatriz', 'Guilherme', 'Mariana'],
        'Qua': ['Isabela', 'Felipe', 'Camila', 'Daniel', 'Gabriela'],
        'Qui': ['Thiago', 'Larissa', 'Eduardo', 'Letícia', 'Matheus'],
        'c': ['José', 'Carolina', 'Marcos', 'Júlia', 'Bruna']
    })

# Função para lidar com as edições
def handle_edit(edits):
    for key, change in edits.items():
        # Tratar chaves não numéricas
        for column, value in change.items():
            st.session_state.df.at[key, column] = value

# Personalizar o estilo da tabela
st.markdown("""
<style>
  div[data-baseweb="data_editor"] table {
    font-size: 16px;
    font-family: 'Arial', sans-serif;
    border-collapse: collapse;
    width: 100%;
  }

  div[data-baseweb="data_editor"] th, div[data-baseweb="data_editor"] td {
    padding: 12px 15px;
    text-align: left;
    border-bottom: 1px solid #ddd;
  }

  div[data-baseweb="data_editor"] th {
    background-color: #f2f2f2;
  }

  div[data-baseweb="data_editor"] input {
    font-size: 16px;
    padding: 8px 12px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
</style>
""", unsafe_allow_html=True)

# Renderizando o DataFrame como editável
edits = st.data_editor(st.session_state.df)
handle_edit(edits)
