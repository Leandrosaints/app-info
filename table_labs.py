import streamlit as st
import pandas as pd

# Criando um exemplo de dataframe com 7 linhas e 5 colunas (dias da semana)
data = {
    'Segunda': [25, 30, 35, 28, 40, 33, 27],
    'Terça': [22, 27, 32, 25, 38, 31, 24],
    'Quarta': [28, 33, 38, 31, 43, 36, 29],
    'Quinta': [20, 25, 30, 23, 35, 28, 21],
    'Sexta': [24, 29, 34, 27, 39, 32, 25]
}
df = pd.DataFrame(data, index=['Lab 01', 'Lab 02', 'Lab 03', 'Lab 04', 'Lab 05', 'Lab 06', 'Lab 07'])

# Função para editar os valores da tabela
def edit_cell(row, col, value):
    df.at[row, df.columns[col]] = value
    return df

# Exibindo o dataframe como uma tabela no Streamlit e permitindo a edição
st.title("Agendamentos de Laboratorios")
edited_df = st.data_editor(df, num_rows="dynamic", use_container_width=True)

# Verificar se a tabela foi editada e atualizar o dataframe
if edited_df is not None:
    df = edited_df
