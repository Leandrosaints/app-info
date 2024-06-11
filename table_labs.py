import streamlit as st
from src.style_header import css_style,hidden_menu
from codes.funcs import add_img_app
from codes.render_table import draw_table
st.set_page_config(layout="wide")
add_img_app('src/img_fundo.jpg')
from datetime import datetime, timedelta

def obter_dias_uteis_semana_atual():
    hoje = datetime.now()
    inicio_semana = hoje - timedelta(days=hoje.weekday())  # Segunda-feira desta semana
    fim_semana = inicio_semana + timedelta(days=4)  # Sexta-feira desta semana

    return [(inicio_semana + timedelta(days=i)).strftime("%d/%m")
            for i in range((fim_semana - inicio_semana).days + 1)
            if (inicio_semana + timedelta(days=i)).weekday() < 5]

# Exemplo de uso
dias_uteis = obter_dias_uteis_semana_atual()


st.markdown(hidden_menu, unsafe_allow_html=True)
text = """
                             🙂 🖥️ 🪛⚙️
    Olá! Bem-vindo ao Sistema Básico de Agendamentos de labs. 
    Esta é uma versão beta, então por favor, tenha paciência, Obrigado 🫡!
"""
st.markdown("<h1 class='title'>Agendamentos de Laboratórios</h1>", unsafe_allow_html=True)
st.markdown(f"<h2 class='user_name'>{text} </h2>", unsafe_allow_html=True)



st.markdown(css_style, unsafe_allow_html=True)
turno = st.selectbox("Selecione o turno:", ["Matutino", "Vespertino"], key='select-box')
save_url = f"http://127.0.0.1:8080/write_data/{turno}"
editable = False#st.checkbox("Permitir Edição")
st.markdown(f'<h4 class="span-aviso"> 👉Agendamentos de {dias_uteis[0]} a {dias_uteis[4]} 📅</h4>', unsafe_allow_html=True)
if draw_table(editable, save_url, turno):
    st.rerun()

#draw_table(table_height=480, editable=editable, save_url=f'https://app-info.onrender.com/write_data/{turno}', turno=turno)
