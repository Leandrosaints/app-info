import streamlit as st
import pandas as pd

# Criando um exemplo de dataframe com 7 linhas e 5 colunas (dias da semana)
data = {
    'LAB': ['LAB AUTOMOTIVA', 'Lab 02', 'Lab 03', 'Lab 04', 'Lab 05', 'Lab 06', 'Lab 07'],
    'Seg': ['prof: Leandro', 'prof: Maria', 'prof: Pedro', 'prof: Ana', 'prof: Lucas', 'prof: Fernanda', 'prof: João'],
    'Ter': ['prof: Leandro', 'prof: Maria', 'prof: Pedro', 'prof: Ana', 'prof: Lucas', 'prof: Fernanda', 'prof: João'],
    'Qua': ['prof: Leandro', 'prof: Maria', 'prof: Pedro', 'prof: Ana', 'prof: Lucas', 'prof: Fernanda', 'prof: João'],
    'Qui': ['prof: Leandro', 'prof: Maria', 'prof: Pedro', 'prof: Ana', 'prof: Lucas', 'prof: Fernanda', 'prof: João'],
    'Sex': ['prof: Leandro', 'prof: Maria', 'prof: Pedro', 'prof: Ana', 'prof: Lucas', 'prof: Fernanda', 'prof: João']
}
df = pd.DataFrame(data)

# Função para editar os valores da tabela
def edit_cell(row, col, value):
    df.at[row, df.columns[col]] = value
    return df

# Exibindo o dataframe como uma tabela no Streamlit e permitindo a edição
st.set_page_config(layout="wide")  # Definir o layout do Streamlit como "wide"
st.title("Agendamentos de Laboratorios")
turno = st.selectbox("Selecione o turno:", ["Matutino", "Vespertino", "Noturno"])
st.write(f"Você selecionou o turno: {turno}")

# Adicionar estilo CSS personalizado
st.markdown("""
<style>
    .dataframe {
        font-size: 14px;
        width: 100%;
        overflow-x: auto;
        white-space: nowrap;
    }
    .dataframe th, .dataframe td {
        padding: 10px;
        text-align: left;
        border-bottom: 1px solid #ddd;
    }
    @media (max-width: 767px) {
        .dataframe {
            font-size: 12px;
            padding: 5px;
        }
        .dataframe th, .dataframe td {
            padding: 5px;
        }
    }
</style>
""", unsafe_allow_html=True)

edited_df = st.data_editor(df, num_rows="dynamic", use_container_width=True)

# Verificar se a tabela foi editada e atualizar o dataframe
if edited_df is not None:
    df = edited_df
