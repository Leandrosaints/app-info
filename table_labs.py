import streamlit as st
from src.style_header import css_style,hidden_menu, prox_style
from codes.funcs import add_img_app
from codes.render_table import draw_table
st.set_page_config(page_title='Agendamentos labs info', page_icon='🖥️',layout="wide")
add_img_app('src/img_fundo.jpg')
from datetime import datetime, timedelta
from datetime import datetime, timedelta


def obter_dias_uteis_proxima_semana(st):
    hoje = datetime.now()

    # Se hoje for quinta-feira, exibir os dias úteis da próxima semana
    if hoje.weekday() == 3:
        inicio_semana = hoje + timedelta(days=3)  # Segunda-feira da próxima semana
        fim_semana = inicio_semana + timedelta(days=5)  # Sexta-feira da próxima semana
        lista_proximos_dias = [(inicio_semana + timedelta(days=i)).strftime("%d/%m")
                             for i in range((fim_semana - inicio_semana).days + 1)
                             if (inicio_semana + timedelta(days=i)).weekday() < 5]
        st.markdown(prox_style, unsafe_allow_html=True)
        st.markdown(
            f'<h4 class="span-aviso-prox"> ⚠️Agendamentos de Seg-{lista_proximos_dias[0]} a Qua-{lista_proximos_dias[2]} livres📅</h4>',
            unsafe_allow_html=True)
    else:
        inicio_semana = hoje - timedelta(days=hoje.weekday())  # Segunda-feira desta semana
        fim_semana = inicio_semana + timedelta(days=4)  # Sexta-feira desta semana
        lista_proximos_dias = [(inicio_semana + timedelta(days=i)).strftime("%d/%m")
                             for i in range((fim_semana - inicio_semana).days + 1)
                             if (inicio_semana + timedelta(days=i)).weekday() < 5]

    return lista_proximos_dias



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



st.markdown(css_style, unsafe_allow_html=True)
turno = st.selectbox("Selecione o turno:", ["Matutino", "Vespertino", "Noturno"], key='select-box')
save_url = f"https://agendamentos-labs-informatica.onrender.com/write_data/{turno}"
editable = False#st.checkbox("Permitir Edição")
obter_dias_uteis_proxima_semana(st)
st.markdown(f'<h4 class="span-aviso"> 👉Agendamentos de {dias_uteis[0]} a {dias_uteis[4]} 📅</h4>', unsafe_allow_html=True)
atualizar = st.button('Atualizar planilha', key='btn-atualizar')
draw_table(editable, save_url, turno)

#draw_table(table_height=480, editable=editable, save_url=f'https://app-info.onrender.com/write_data/{turno}', turno=turno)
