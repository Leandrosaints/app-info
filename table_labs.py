import streamlit as st
from src.style_header import css_style,hidden_menu, prox_style
from codes.funcs import add_img_app
from codes.render_table import draw_table
st.set_page_config(page_title='Agendamentos labs info', page_icon='🖥️',layout="wide")
add_img_app('src/img_fundo.jpg')
import streamlit as st
from datetime import datetime, timedelta
def obter_dias_uteis_proxima_semana(st):
    hoje = datetime.now()

    if hoje.weekday() == 3:  # Se hoje for quinta-feira
        inicio_semana = hoje + timedelta(days=4)  # Segunda-feira da próxima semana
        fim_semana = inicio_semana + timedelta(days=2)  # Quarta-feira da próxima semana
        lista_proximos_dias = [
            (inicio_semana + timedelta(days=i)).strftime("%d/%m")
            for i in range((fim_semana - inicio_semana).days + 1)
            if (inicio_semana + timedelta(days=i)).weekday() < 5
        ]
        st.markdown(prox_style, unsafe_allow_html=True)
        st.markdown(
            f'<h4 class="span-aviso-prox"> ⚠️Agendamentos de {lista_proximos_dias[0]} a {lista_proximos_dias[2]} livres📅</h4>',
            unsafe_allow_html=True
        )
    else:
        inicio_semana = hoje - timedelta(days=hoje.weekday())  # Segunda-feira desta semana
        fim_semana = inicio_semana + timedelta(days=4)  # Sexta-feira desta semana
        lista_proximos_dias = [
            (inicio_semana + timedelta(days=i)).strftime("%d/%m")
            for i in range((fim_semana - inicio_semana).days + 1)
            if (inicio_semana + timedelta(days=i)).weekday() < 5
        ]

    return lista_proximos_dias
# Exemplo de uso
#lista_proximos_dias = obter_dias_uteis_proxima_semana()
iframe = """<iframe class="icon" src="https://lottie.host/embed/ef00d3f0-670a-4b30-8aee-e85886b4914d/PXvkh2M43V.json" width="30" height="30" frameborder="0" allowfullscreen></iframe>"""

def obter_dias_uteis_semana_atual():
    hoje = datetime.now()

    # Cria um objeto para sexta-feira às 17h da semana atual
    sexta_17h = hoje.replace(hour=17, minute=0, second=0, microsecond=0)

    # Verifica se é quinta-feira
    if hoje.weekday() == 3:
        # Ajusta a data para a próxima segunda-feira e próxima quinta-feira
        segunda_proxima = hoje + timedelta(days=(7 - hoje.weekday()))
        quinta_proxima = segunda_proxima + timedelta(days=3)

        dias_uteis = [(segunda_proxima + timedelta(days=i)).strftime("%d/%m")
                      for i in range((quinta_proxima - segunda_proxima).days + 1)
                      if (segunda_proxima + timedelta(days=i)).weekday() < 5]

        # Exibe as datas no formato markdown com st.markdown

        seg_prox = dias_uteis[0]
        quinta_prox = dias_uteis[-1]
        st.markdown(
            f'<h4 class="span-aviso-prox" class="container"> {iframe} Agendamentos de {seg_prox} a {quinta_prox} 📅</h4>',
            unsafe_allow_html=True)

        return dias_uteis

    # Verifica se é sexta-feira após as 17h ou qualquer dia após sexta-feira
    if hoje.weekday() > 4 or (hoje.weekday() == 4 and hoje >= sexta_17h):
        # Ajusta a data para a próxima segunda-feira
        dias_para_proxima_segunda = 7 - hoje.weekday()
        hoje += timedelta(days=dias_para_proxima_segunda)

    # Calcula o início e fim da semana útil (segunda a sexta)
    inicio_semana = hoje - timedelta(days=hoje.weekday())  # Segunda-feira desta semana
    fim_semana = inicio_semana + timedelta(days=4)  # Sexta-feira desta semana

    # Cria a lista de datas úteis
    dias_uteis = [(inicio_semana + timedelta(days=i)).strftime("%d/%m")
                  for i in range((fim_semana - inicio_semana).days + 1)
                  if (inicio_semana + timedelta(days=i)).weekday() < 5]

    return dias_uteis


# Testando a função
dias_uteis = obter_dias_uteis_semana_atual()

st.markdown(hidden_menu, unsafe_allow_html=True)
text = """
                             🙂 🖥️ 🪛⚙️
    Olá! Bem-vindo ao Sistema Básico de Agendamentos de labs. 
    Esta é uma versão beta, então por favor, tenha paciência, Obrigado 🫡!
"""
# Adicionar o Lottie como ícone

st.markdown("<h1 class='title'>Agendamentos de Laboratórios</h1>", unsafe_allow_html=True)
st.markdown(f"<h2 class='user_name'>{text} </h2>", unsafe_allow_html=True)

with st.expander('Dicas Rapidas❓', expanded=True):
    st.markdown("""
         <div class='poup-up' style='padding: 20px; background-color:#f0f2f6; border-radius: 10px;'>
             <h3> Dicas Rápidas de Uso  </h3>
             <ul style='list-style-type: disc; padding-left: 20px;'>
                 <li>Insira Apenas o Primeiro Nome: Não é necessário usar prefixos como Prof. ou Professor, pois o sistema já os adiciona automaticamente.</li>
                 <li>Atualize a Planilha ao Entrar: Sempre que entrar no sistema, atualize a tabela para verificar a disponibilidade correta das salas.</li>
                 <li>Atualize a Planilha Após Agendar: Após terminar de agendar, clique em "Atualizar planilha" para que os dados sejam refletidos no sistema.</li>
             </ul>
         </div>
     """, unsafe_allow_html=True)



st.markdown(css_style, unsafe_allow_html=True)
turno = st.selectbox("Selecione o turno:", ["Matutino", "Vespertino", "Noturno"], key='select-box')
save_url = f"https://app-info.onrender.com/write_data/{turno}"
editable = False#st.checkbox("Permitir Edição")
#obter_dias_uteis_proxima_semana(st)
try:
    st.markdown(f'<h4 class="span-aviso" class="container"> {iframe} Agendamentos de {dias_uteis[0]} a {dias_uteis[4]} 📅</h4>', unsafe_allow_html=True)
except:
    pass
atualizar = st.button('Atualizar planilha', key='btn-atualizar')

draw_table(editable, save_url, turno)

#draw_table(table_height=480, editable=editable, save_url=f'https://app-info.onrender.com/write_data/{turno}', turno=turno)
