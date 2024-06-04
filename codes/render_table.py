import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import requests
def saveDataToJSON(df, save_url):
    requests.post(save_url, json=df.to_dict('records'))

def fetch_sheet_data(turno):
    response = requests.get(f"http://127.0.0.1:8080/read_data/{turno}")
    if response.status_code == 200:
        return response.json()["values"]
    else:
        st.error("Desculpe, houve um erro no sistema, contacte os responsáveis.")
        return []
def draw_table(table_height, editable, save_url, turno):
    data = fetch_sheet_data(turno)
    dias_da_semana = ["LAB", "Seg", "Ter", "Qua", "Qui", "Sex"]
    df = pd.DataFrame(data, columns=dias_da_semana)
    columns = df.columns

    thead1 = "<thead><tr><th style='background-color:#098aff;'scope='col'></th>"
    thead_temp = ["<th style='background-color:#098aff;'scope='col'>" + str(col) + "</th>" for col in columns]
    header = thead1 + "".join(thead_temp) + "</tr ></thead>"

    rows = ["<tr><th scope='row'></th>" for _ in range(df.shape[0])]
    cells = []
    for i, row in enumerate(df.values.tolist()):
        row_cells = []
        for j, value in enumerate(row):
            if str(value).lower() == 'livre':
                if editable:
                    row_cells.append(f"<td><button style='background-color:#1ef79399; color:black;' class='btn btn-success' onclick='openModal({i}, {j}, \"{df.columns[j]}\")'>Livre</button></td>")
                else:

                    row_cells.append(f"<td style='background-color:#1ef79399; color:black;'>Livre</td>")
            elif 'prof' in str(value).lower():
                row_cells.append(f"<td style='background-color: yellow;'>{value}</td>")
            else:
                if editable and str(value).lower() != 'livre':
                    with st.form(key=f"form_{i}_{j}"):
                        new_value = st.text_input(f"Celula ({i},{j})", value=value, key=f"input_{i}_{j}")
                        if st.form_submit_button("Salvar"):
                            df.at[i, df.columns[j]] = new_value
                            saveDataToJSON(df, save_url)
                    row_cells.append(f"<td style='background-color:#b6b6be; color:white;'>{new_value}</td>")
                else:
                    row_cells.append(f"<td style='background-color:#b6b6be; color:white;'>{value}</td>")
        cells.append("".join(row_cells))
    body = "".join([rows[i] + cells[i] + "</tr>" for i in range(df.shape[0])])

    table_html = f"""
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
    <style>
        /* Estilos da tabela, mantidos iguais */
    </style>
    <div class="table-responsive">
        <table class="table table-bordered table-sm text-center">
            {header}
            <tbody>
                {body}
            </tbody>
        </table>
    </div>
    """
    return components.html(table_html, height=table_height, scrolling=True)

st.title('Tabela Interativa')
turno = st.selectbox("Selecione o turno:", ["Matutino", "Vespertino"])
editable = st.checkbox("Permitir Edição")
save_url = f"http://127.0.0.1:8080/write_data/{turno}"

draw_table(600, editable, save_url, turno)
