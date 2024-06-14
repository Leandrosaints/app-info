import time

import streamlit as st
from src.style_header import css_style,hidden_menu, prox_style
from codes.funcs import add_img_app
from codes.render_table import draw_table
st.set_page_config(page_title='Agendamentos labs', page_icon='🖥️',layout="wide")
add_img_app('src/img_fundo.jpg')
from datetime import datetime, timedelta
from codes.dias import obter_dias_uteis_proxima_semana
# Exemplo de uso
#lista_proximos_dias = obter_dias_uteis_proxima_semana()


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

with st.expander('Dicas Rapidas❓', expanded=False):

    st.markdown("""
         <div class='poup-up' style='padding: 20px; background-color:#f0f2f6; border-radius: 10px;'>
             <h3> Dicas Rápidas de Uso  </h3>
             <ul style='list-style-type: disc; padding-left: 20px;'>
                 <li>Insira Apenas o Primeiro Nome: Não é necessário usar prefixos como Prof. ou Professor, pois o sistema já os adiciona automaticamente.</li>
                 <li>Atualize a Planilha ao Entrar: Sempre que entrar no sistema, atualize a planilha para verificar a disponibilidade correta das salas.</li>
                 <li>Atualize a Planilha Após Agendar: Após terminar de agendar, clique em "Atualizar planilha" para que os dados sejam refletidos no sistema.</li>
             </ul>
         </div>
     """, unsafe_allow_html=True)



st.markdown(css_style, unsafe_allow_html=True)
turno = st.selectbox("Selecione o turno:", ["Matutino", "Vespertino", "Noturno"], key='select-box')
save_url = f"https://agendamentos-labs-informatica.onrender.com/write_data/{turno}"
editable = False#st.checkbox("Permitir Edição")
obter_dias_uteis_proxima_semana(st, prox_style)

st.markdown(f'<h4 class="span-aviso" class="container"> 👉Agendamentos de {dias_uteis[0]} a {dias_uteis[4]} 📅</h4>', unsafe_allow_html=True)
atualizar = st.button('Atualizar planilha', key='btn-atualizar')

draw_table(editable, save_url, turno)

#draw_table(table_height=480, editable=editable, save_url=f'https://app-info.onrender.com/write_data/{turno}', turno=turno)

