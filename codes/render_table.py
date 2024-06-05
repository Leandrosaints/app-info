import streamlit as st
import pandas as pd
import requests
import streamlit.components.v1 as components

# Função para salvar os dados no servidor
def saveDataToJSON(df, save_url):
    try:
        response = requests.post(save_url, json=df.to_dict('records'))
        if response.status_code != 200:
            st.error("Erro ao salvar os dados.")
    except Exception as e:
        st.error(f"Erro: {e}")

# Função para buscar dados do servidor
def fetch_sheet_data(turno):
    try:
        response = requests.get(f"http://127.0.0.1:8080/read_data/{turno}")
        if response.status_code == 200:
            return response.json()["values"]
        else:
            st.error("Desculpe, houve um erro no sistema, contacte os responsáveis.")
            return []
    except Exception as e:
        st.error(f"Erro: {e}")
        return []

# Função para atualizar o valor da célula clicada
def update_cell_value(df, row, col, new_value):
    dias_da_semana = ["LAB", "Seg", "Ter", "Qua", "Qui", "Sex"]
    df.at[row, dias_da_semana[col]] = new_value
    return df

# Função para desenhar a tabela
def draw_table(table_height, editable, save_url, turno):
    data = fetch_sheet_data(turno)
    dias_da_semana = ["LAB", "Seg", "Ter", "Qua", "Qui", "Sex"]
    df = pd.DataFrame(data, columns=dias_da_semana)

    # Estado para armazenar a célula que está sendo editada
    if 'editing_cell' not in st.session_state:
        st.session_state.editing_cell = (-1, -1)

    def handle_click(row, col, df):
        st.session_state.editing_cell = (row, col)
        new_value = st.text_input("Novo valor:", value=df.iloc[row, col], key=f"input_{row}_{col}")
        if st.button("Salvar", key=f"save_{row}_{col}"):
            dft = update_cell_value(df, row, col, new_value)
            saveDataToJSON(df, save_url)
            st.session_state.editing_cell = (-1, -1)

    # Renderizar a tabela
    st.write("### Tabela")

    styled_df = df.style.applymap(
        lambda val: 'background-color: #1ef79399; color:black;' if str(val).lower() == 'livre' else
                    'background-color: yellow; color:black;' if 'prof' in str(val).lower() else '',
        subset=dias_da_semana
    ).set_properties(**{'text-align': 'center'})

    if st.session_state.editing_cell != (-1, -1):
        row, col = st.session_state.editing_cell
        styled_df = styled_df.apply(lambda x: ['background-color: #ffff00' if x.name == row and x.name == dias_da_semana[col] else '' for _ in range(len(x))], axis=1)

    st.write(styled_df)

st.title('Tabela Interativa')
turno = st.selectbox("Selecione o turno:", ["Matutino", "Vespertino"])
editable = st.checkbox("Permitir Edição")
save_url = f"http://127.0.0.1:8080/write_data/{turno}"

draw_table(600, editable, save_url, turno)
