# app.py
import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from auth_user import handle_authentication
st.set_page_config(layout="wide")
# Chama a função para manipular a autenticação
user_info = handle_authentication()

# Criando um exemplo de dataframe com 7 linhas e 5 colunas (dias da semana)
data = {
    'LAB': ['LAB AUTOMOTIVA', 'Lab 02', 'Lab 03', 'Lab 04', 'Lab 05', 'Lab 06', 'Lab 07'],
    'Seg': ['prof: Leandro', 'prof: Maria', 'prof: Pedro', 'prof: Ana', 'prof: Lucas', 'prof: Fernanda', 'prof: João'],
    'Ter': ['livre', 'prof: Maria', 'prof: Pedro', 'prof: Ana', 'prof: Lucas', 'prof: Fernanda', 'prof: João'],
    'Qua': ['prof: Leandro', 'prof: Maria', 'prof: Pedro', 'prof: Ana', 'prof: Lucas', 'prof: Fernanda', 'prof: João'],
    'Qui': ['prof: Leandro', 'prof: Maria', 'prof: Pedro', 'prof: Ana', 'prof: Lucas', 'prof: Fernanda', 'prof: João'],
    'Sex': ['livre', 'livre', 'livre', 'livre', 'livre', 'livre', 'livre']
}
df = pd.DataFrame(data)


# Função para desenhar a tabela com Bootstrap
def draw_table(df, table_height):
    columns = df.columns

    # Construir o cabeçalho da tabela
    thead1 = "<thead><tr><th scope='col'>#</th>"
    thead_temp = ["<th scope='col'>" + str(col) + "</th>" for col in columns]
    header = thead1 + "".join(thead_temp) + "</tr></thead>"

    # Construir o corpo da tabela
    rows = ["<tr><th scope='row'>" + str(i + 1) + "</th>" for i in range(df.shape[0])]
    cells = []
    for row in df.values.tolist():
        row_cells = []
        for value in row:
            if str(value).lower() == 'livre':
                row_cells.append(
                    f"<td><input type='text' value='{value}' class='form-control' style='background-color: green; color: white;'></td>")

            else:
                row_cells.append(f"<td><input type='text' value='{value}' class='form-control'></td>")
        cells.append("".join(row_cells))
    body = "".join([rows[i] + cells[i] + "</tr>" for i in range(df.shape[0])])

    # Montar a tabela completa
    table_html = f"""
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
    <table class="table table-bordered text-center ">
        {header}
        <tbody>
            {body}
        </tbody>
    </table>
    """

    return components.html(table_html, height=table_height, scrolling=True)


# Exibindo o dataframe como uma tabela no Streamlit e permitindo a edição

st.title("Agendamentos de Laboratórios")
turno = st.selectbox("Selecione o turno:", ["Matutino", "Vespertino", "Noturno"])
st.write(f"Você selecionou o turno: {turno}")

if user_info:
    st.write(f"Bem-vindo, {user_info['name']}!")
    st.write(f"Seu email é: {user_info['email']}")

    # Exibir a tabela apenas se o usuário estiver autenticado
    edited_df = draw_table(df, table_height=400)
else:
    st.write("Por favor, faça login para continuar.")
