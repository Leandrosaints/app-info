import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from auth_user import handle_authentication

# Chama a função para manipular a autenticação
user_info = handle_authentication()
st.set_page_config(layout="wide")
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

# Função para desenhar a tabela com Bootstrap e habilitar edição ao clicar em "livre"
def draw_table(df, table_height, editable):
    columns = df.columns

    # Construir o cabeçalho da tabela
    thead1 = "<thead><tr><th scope='col'>#</th>"
    thead_temp = ["<th scope='col'>" + str(col) + "</th>" for col in columns]
    header = thead1 + "".join(thead_temp) + "</tr></thead>"

    # Construir o corpo da tabela
    rows = ["<tr><th scope='row'>" + str(i+1) + "</th>" for i in range(df.shape[0])]
    cells = []
    for row in df.values.tolist():
        row_cells = []
        for col, value in enumerate(row):
            if str(value).lower() == 'livre':
                row_cells.append(f"<td><button class='btn btn-success' onclick='openModal({row.index(value)}, this)'>{value}</button></td>")
            elif 'prof' in str(value).lower():
                row_cells.append(f"<td style='background-color: yellow;'>{value}</td>")

            else:
                row_cells.append(f"<td>{value}</td>")
        cells.append("".join(row_cells))
    body = "".join([rows[i] + cells[i] + "</tr>" for i in range(df.shape[0])])

    # Montar a tabela completa com modal
    table_html = f"""
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
    <script>
        function openModal(index, element) {{
            var modal = new bootstrap.Modal(document.getElementById('editModal'));
            document.getElementById('modalIndex').value = index;
            document.getElementById('modalValue').value = element.textContent;
            modal.show();
        }}
        function saveValue() {{
            var index = document.getElementById('modalIndex').value;
            var value = document.getElementById('modalValue').value;
            document.querySelectorAll('tbody tr')[index].querySelectorAll('td')[{columns.get_loc('Ter')}].innerHTML = value;
        }}
    </script>
    <table class="table table-bordered text-center">
        {header}
        <tbody>
            {body}
        </tbody>
    </table>
    <div class="modal fade" id="editModal" tabindex="-1" aria-labelledby="editModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="editModalLabel">Editar Valor</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <input type="hidden" id="modalIndex">
                    <div class="mb-3">
                        <label for="modalValue" class="form-label">Novo Valor</label>
                        <input type="text" class="form-control" id="modalValue">
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Fechar</button>
                    <button type="button" class="btn btn-primary" onclick="saveValue()">Salvar</button>
                </div>
            </div>
        </div>
    </div>
    """

    return components.html(table_html, height=table_height, scrolling=True)

# Verifica se o usuário está autenticado
if user_info:
    st.write(f"Olá, {user_info['name']} ({user_info['email']})!")
    st.success("Você está logado.")
    editable = True





st.title("Agendamentos de Laboratórios")
turno = st.selectbox("Selecione o turno:", ["Matutino", "Vespertino", "Noturno"])
st.write(f"Você selecionou o turno: {turno}")

# Aplicar o estilo da tabela com Bootstrap
draw_table(df, table_height=400, editable=editable)
