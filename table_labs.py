import streamlit as st
from src.style_header import css_style, hidden_menu, prox_style
from codes.funcs import add_img_app
from codes.render_table import draw_table
from datetime import datetime, timedelta

st.set_page_config(page_title='Agendamentos labs info', page_icon='🖥️', layout="wide")
add_img_app('src/img_fundo.jpg')
fast = """<iframe src="https://lottie.host/embed/8bbe00c3-6a0f-480a-8a9c-1c3a3b4ca0b3/J8xLuufEsY.json" width="100" height="70" frameborder="0" allowfullscreen></iframe>"""
calendar = """<iframe src="https://lottie.host/embed/db85baef-ab6d-435a-8d62-fdda70e4ee7e/n5NDUXZy8m.json" width="50" height="50" frameborder="0" allowfullscreen></iframe>"""
iframe = """<iframe class="icon" src="https://lottie.host/embed/ef00d3f0-670a-4b30-8aee-e85886b4914d/PXvkh2M43V.json" width="50" height="50" frameborder="0" allowfullscreen></iframe>"""
dicas = """<iframe src="https://lottie.host/embed/00f24db4-0620-426d-a7a7-c0c654fd736d/8OhHVJTY3m.json"></iframe>"""
engrenagem = """<iframe src="https://lottie.host/embed/5b711b44-5a40-4fe4-810b-9667cdf50cd3/CDcya5jczW.json"></iframe>"""
education = """<iframe src="https://lottie.host/embed/de539e29-e949-4f1c-a4b9-280dac8b715b/aMTJ96nPIP.json" width="60" height="60" frameborder="0" allowfullscreen></iframe>"""
prof = """<iframe src="https://lottie.host/embed/eb77a318-ea8b-4597-b77d-9b2dcf8bf2c7/hMOVLS0Zex.json"></iframe>"""
capelo = """<iframe src="https://lottie.host/embed/4d7db023-d7fd-4148-8bd5-2416a50eb723/DhI1FFjxft.json"></iframe>"""
gost = """<iframe src="https://lottie.host/embed/a046c316-bdcf-49cc-a72b-5e7d4694aac0/HrqbNciMBU.json" width="60" height="60" frameborder="0" allowfullscreen></iframe>"""
bot = """<iframe src="https://lottie.host/embed/1c566895-3760-446f-be65-4e5844bb3716/pqYAqufAFV.json" width="80" height="100" frameborder="0" allowfullscreen></iframe>"""
alien = """<iframe src="https://lottie.host/embed/eb14cfd3-693a-456f-9488-a45a7fc9925d/k8IUvM5I4m.json" width="80" height="100" frameborder="0" allowfullscreen></iframe>"""
point = """<iframe src="https://lottie.host/embed/9b0b1e7c-10d7-4ed3-93df-87b4298759c1/2JovVu7qlh.json" width="100" height="80" frameborder="0" allowfullscreen></iframe>"""
st.markdown(f'<span class="st-emotion-cache-18ni7ap ezrtsby2">{education} {engrenagem} {dicas} {capelo}</span>',unsafe_allow_html=True)
def obter_dias_uteis_proxima_semana():
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
            f'<div class="span-aviso" id="container-aviso"> {calendar} Agendamentos de {lista_proximos_dias[0]} a {lista_proximos_dias[2]} livres📅</div>',
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
            f'<div class="span-aviso" id="container-aviso"> {calendar} Agendamentos de {seg_prox} a {quinta_prox} </div>',
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

# Layout para botões de turno


editable = False

try:
    st.markdown(f'<div class="span-aviso" id="container-aviso"> {calendar} Agendamentos de {dias_uteis[0]} a {dias_uteis[4]}</div>', unsafe_allow_html=True)
except:
    pass

st.markdown(f'<span class="turno-one">Escolha um Período abaixo</span>', unsafe_allow_html=True)

def views_iframe(iframe):
    st.markdown(f"<div class='stAlert'>{iframe}</div>",unsafe_allow_html=True)

# Inicializar a variável para armazenar o turno selecionado
turno = st.session_state.get('turno', 'Matutino')

col1, col2, col3, col4 = st.columns(4)

# Placeholders for each button
placeholder1 = col1.empty()
placeholder2 = col2.empty()
placeholder3 = col3.empty()
placeholder4 = col4.empty()

# Button click handlers
if placeholder1.button("Matutino"):
    turno = "Matutino"
    st.session_state['turno'] = turno
    st.warning(f'Esta editando e vizualiando Periodo  {turno}', icon="⚠️")


if placeholder2.button("Vespertino"):
    turno = "Vespertino"
    st.session_state['turno'] = turno
    st.warning(f'Esta editando e vizualiando Periodo {turno}', icon="⚠️")

if placeholder3.button("Noturno"):
    turno = "Noturno"
    st.session_state['turno'] = turno
    st.warning(f'Esta editando e vizualiando o Periodo  {turno}', icon="⚠️")

if placeholder4.button('Atualizar planilha'):
    # Faça algo aqui para atualizar a planilha
    pass


save_url = f"https://agendamentos-labs-informatica.onrender.com/write_data/{turno}"
# Usar o turno selecionado para desenhar a tabela
draw_table(editable, save_url, turno)

#draw_table(table_height=480, editable=editable, save_url=f'https://app-info.onrender.com/write_data/{turno}', turno=turno)
