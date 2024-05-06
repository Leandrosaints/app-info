import json
import streamlit as st

# Dados JSON
json_data = '''
{
    "lab01": {
        "nome": "Laboratorio 01",
        "N_maquinas": 30,
        "softweres_instalados": ["office 365", "Fusion", "arduino", "lego", "chrome", "chrome"]
    }
}
'''


# Carregar os dados do JSON
data_dict = json.loads(json_data)

# Função para filtrar os dados
def filter_data(search_term):

    if search_term:
        results = {key: value for key, value in data_dict.items() if search_term.lower() in str(value).lower()}

    else:
        results = data_dict
    return results

# Função principal para a barra de pesquisa
def search_bar():
    # Inicializar st.session_state.searched se ainda não estiver inicializado
    if "searched" not in st.session_state:
        st.session_state.searched = ""

    # Barra de pesquisa
    search_term = st.text_input("Pesquisar:")

    # Verificar se o Enter foi pressionado
    if st.session_state.searched != search_term:
        st.session_state.searched = search_term


    # Filtrar os dados com base no termo de pesquisa
    filtered_data = filter_data(st.session_state.searched)

    # Exibir os resultados apenas quando o Enter for pressionado
    if st.session_state.searched:
        if filtered_data:
            #st.write("Resultados da pesquisa:")
            for value in filtered_data.items():
                st.write(f"{value}")
        else:
            st.write("Nenhum resultado encontrado.")

# Executar a função de pesquisa

