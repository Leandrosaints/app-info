import streamlit as st

# Criar a tabela
st.title("Tabela de Agendamentos")

# Dias da semana
dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira"]

# Criar a tabela
table = st.empty()

with table.container():
    cols = st.columns(len(dias_semana))
    for col, dia in zip(cols, dias_semana):
        with col:
            st.write(dia)

    # Linha com o subtítulo "Matutino"
    row = st.columns(len(dias_semana))

    st.write("Matutino")

    # Células editáveis
    for i in range(5):
        row = st.columns(len(dias_semana))
        for j, _ in enumerate(dias_semana):
            with row[j]:
                st.text_area("", key=f"matutino-{j}-{i}", height=100)
