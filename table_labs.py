import streamlit as st
import pandas as pd
from auth_user import handle_authentication
import json
import os

st.set_page_config(layout="wide")
user_info = handle_authentication()

# Function to define the background color of cells
def get_cell_background(value):
    if str(value).lower() == 'livre':
        return 'background-color: green'
    elif 'prof:' in str(value):
        return 'background-color: yellow'
    else:
        return 'background-color: white'

# Function to load data from the JSON file
def load_data():
    try:
        if os.path.exists('data.json'):
            with open('data.json', 'r') as f:
                data = json.load(f)
            return pd.DataFrame(data)
        else:
            # If the file does not exist, return a DataFrame with default data
            return None  # pd.DataFrame(data)
    except (FileNotFoundError, json.JSONDecodeError, IOError) as e:
        st.error(f"Erro ao carregar os dados: {str(e)}")
        return pd.DataFrame(data)

# Load data from JSON file
df = load_data()

def save_changes(edited_df):
    # Save data to JSON file
    try:
        data = edited_df.to_dict('records')
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)
        st.success("Alterações salvas com sucesso!", icon="✅")
    except (IOError, json.JSONDecodeError) as e:
        st.error(f"Erro ao salvar as alterações: {str(e)}")

# Display the DataFrame as a table in Streamlit and allow editing
st.title("Agendamentos de Laboratórios")
turno = st.selectbox("Selecione o turno:", ["Matutino", "Vespertino", "Noturno"])
st.write(f"Você selecionou o turno: {turno}")

if user_info:
    st.write(f"Bem-vindo, {user_info['name']}!")
    st.write(f"Seu email é: {user_info['email']}")

    if df is not None:
        # Apply styles to the DataFrame
        styled_df = df.style.applymap(get_cell_background)

        # Display the styled DataFrame
        st.write(styled_df, height=400, use_container_width=True)

        # Display an editable version of the DataFrame (without styles)
        edited_df = st.experimental_data_editor(df)

        if st.button("Salvar Alterações"):
            save_changes(edited_df)
    else:
        st.write("Nenhum dado disponível para exibir.")
else:
    st.write("Por favor, faça login para continuar.")
