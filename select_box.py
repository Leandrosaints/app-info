import json
import streamlit as st
from codes.files import json_data

# Converter JSON em um dicionário Python
data_dict = json.loads(json_data)
# Lista de laboratórios disponíveis
labs = list(data_dict.keys())
# Menu selecionável
lab_selecionado = st.selectbox('Selecione um laboratório:', labs)

# Exibir resultado com base no laboratório selecionado
if lab_selecionado:
    lab_info = data_dict[lab_selecionado]
    st.write(f'Nome do Laboratório: {lab_info["nome"]}')
    st.write(f'Número de Máquinas: {lab_info["N_maquinas"]}')
    st.write('Softwares Instalados:')
    for software in lab_info["softweres_instalados"]:
        st.write(f'- {software}')
