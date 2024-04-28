import pandas as pd

#https://docs.google.com/spreadsheets/d/18mk1naW5JCQ1o7uNHVhPlvrMdcQ9xdkWQSBqYouP8Pw/edit#gid=1614386316

import streamlit as st

def main():
    st.title("Visualizador de Dados do Google Sheets")

    # URL pública da planilha do Google Sheets (compartilhada como CSV)

    sheet_id = "18mk1naW5JCQ1o7uNHVhPlvrMdcQ9xdkWQSBqYouP8Pw"
    df = pd.read_csv(f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv')




    # Exibir os dados na forma de tabela
    st.write("### Dados da Planilha")
    st.write(df)

    # Exibir uma descrição estatística resumida dos dados
    st.write("### Resumo Estatístico")
    st.write(df.describe())
    """git init 
git add README.md 
git commit -m "primeiro commit" 
git branch -M main 
git remote add origin https://github.com/Leandrosaints/app-info.git
 git push -u origem principa
""" Exibir uma seleção de colunas específicas
    selected_columns = st.multiselect("Selecione as Colunas", df.columns)
    if selected_columns:
        st.write("### Seleção de Colunas")
        st.write(df[selected_columns])

    # Exibir um gráfico de barras para uma coluna específica
    selected_column_bar = st.selectbox("Selecione uma Coluna para Gráfico de Barras", df.columns)
    if selected_column_bar:
        st.write("### Gráfico de Barras")
        st.bar_chart(df[selected_column_bar].value_counts())

    # Exibir um gráfico de dispersão para duas colunas específicas
    selected_column_x = st.selectbox("Selecione a Coluna X para Gráfico de Dispersão", df.columns)
    selected_column_y = st.selectbox("Selecione a Coluna Y para Gráfico de Dispersão", df.columns)
    if selected_column_x and selected_column_y:
        st.write("### Gráfico de Dispersão")
        st.write(df.plot.scatter(x=selected_column_x, y=selected_column_y))

if __name__ == "__main__":
    main()
