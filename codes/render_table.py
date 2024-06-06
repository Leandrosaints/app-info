import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, JsCode
import requests

# Função para salvar os dados no servidor
def saveDataToJSON(df, save_url):
    try:
        json_data = df.to_dict(orient='records')  # Converte o DataFrame para uma lista de dicionários
        response = requests.post(save_url, json=json_data)
        if response.status_code != 200:
            st.error("Erro ao salvar os dados.")
        else:
            st.success("Dados salvos com sucesso.")
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

# Função para desenhar a tabela
def draw_table(editable, save_url, turno):
    # Usando st.session_state para armazenar dados originais e editados
    if 'original_data' not in st.session_state:
        st.session_state.original_data = {}
    if 'edited_data' not in st.session_state:
        st.session_state.edited_data = {}
    if 'data_modified' not in st.session_state:
        st.session_state.data_modified = False

    # Carregar dados apenas se o turno mudou ou se é a primeira vez
    if turno not in st.session_state.original_data:
        data = fetch_sheet_data(turno)
        dias_da_semana = ["LAB", "Seg", "Ter", "Qua", "Qui", "Sex"]
        st.session_state.original_data[turno] = pd.DataFrame(data, columns=dias_da_semana)
        st.session_state.edited_data[turno] = st.session_state.original_data[turno].copy()
    else:
        data = st.session_state.edited_data[turno]

    df = pd.DataFrame(data)

    # Garantir que os nomes das colunas sejam mantidos corretamente
    dias_da_semana = ["LAB", "Seg", "Ter", "Qua", "Qui", "Sex"]
    df.columns = dias_da_semana

    st.write("### Tabela")

    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_default_column(editable=editable)

    # Definindo estilos personalizados
    cell_style_jscode = JsCode("""
    function(params) {
        if (params.value.toLowerCase() === 'livre') {
            return {'color': 'black', 'backgroundColor': '#1ef79399'};
        } else if (params.value.toLowerCase().includes('prof')) {
            return {'color': 'black', 'backgroundColor': 'yellow'};
        } else {
            return null;
        }
    };
    """)

    # Aplicando o estilo para todas as colunas
    for column in df.columns:
        gb.configure_column(column, cellStyle=cell_style_jscode)

    grid_options = gb.build()

    grid_response = AgGrid(
        df,
        gridOptions=grid_options,
        editable=editable,
        height=600,
        theme='streamlit',
        allow_unsafe_jscode=True,  # Permitir uso seguro de JsCode
    )

    # Dataframe com as edições feitas
    edited_df = pd.DataFrame(grid_response['data'])

    # Comparar os dados para detectar mudanças
    if not edited_df.equals(st.session_state.edited_data[turno]):
        st.session_state.edited_data[turno] = edited_df.copy()
        st.session_state.data_modified = True

    # Salvar os dados modificados quando o usuário pressionar o botão
    if st.session_state.data_modified and st.button("Salvar Alterações"):
        saveDataToJSON(st.session_state.edited_data[turno], save_url)
        # Após salvar, atualizar os dados originais e resetar o estado de modificação
        st.session_state.original_data[turno] = st.session_state.edited_data[turno].copy()
        st.session_state.data_modified = False

    return edited_df

st.title('Tabela Interativa')
turno = st.selectbox("Selecione o turno:", ["Matutino", "Vespertino"])
editable = st.checkbox("Permitir Edição")
save_url = f"http://127.0.0.1:8080/write_data/{turno}"

draw_table(editable, save_url, turno)
