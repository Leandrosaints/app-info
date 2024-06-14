from datetime import datetime, timedelta

def obter_dias_uteis_proxima_semana(st, style):
    hoje = datetime.now()

    if hoje.weekday() == 3:  # Se hoje for quinta-feira
        segunda_proxima_semana = hoje + timedelta(days=4)  # Segunda-feira da próxima semana
        quarta_proxima_semana = hoje + timedelta(days=6)  # Quarta-feira da próxima semana
        lista_proximos_dias = [
            segunda_proxima_semana.strftime("%d/%m"),
            quarta_proxima_semana.strftime("%d/%m")
        ]
        st.markdown(style, unsafe_allow_html=True)
        st.markdown(
            f'<h4 class="span-aviso-prox"> ⚠️Agendamentos de Seg-{lista_proximos_dias[0]} a Qua-{lista_proximos_dias[1]} livres📅</h4>',
            unsafe_allow_html=True
        )
    elif hoje.weekday() == 4:  # Se hoje for sexta-feira
        segunda_proxima_semana = hoje + timedelta(days=3)  # Segunda-feira da próxima semana
        quinta_proxima_semana = hoje + timedelta(days=6)  # Quinta-feira da próxima semana
        lista_proximos_dias = [
            segunda_proxima_semana.strftime("%d/%m"),
            quinta_proxima_semana.strftime("%d/%m")
        ]
        st.markdown(style, unsafe_allow_html=True)
        st.markdown(
            f'<h4 class="span-aviso-prox"> ⚠️Agendamentos de Seg-{lista_proximos_dias[0]} a Qui-{lista_proximos_dias[1]} livres📅</h4>',
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
