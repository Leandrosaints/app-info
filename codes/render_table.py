import streamlit as st
import pandas as pd
import requests
import streamlit.components.v1 as components

# Constantes e Configurações
DIAS_DA_SEMANA = ["LAB", "Seg", "Ter", "Qua", "Qui", "Sex"]

# Função para salvar os dados no servidor
def save_data_to_json(df, save_url):
    json_data = df.to_dict(orient='records')
    response = requests.post(save_url, json=json_data)
    st.write(response.json())

# Função para buscar dados do servidor
def fetch_sheet_data(turno):
    try:#https://agendamentos-labs-informatica.onrender.com
        response = requests.get(f"https://agendamentos-labs-informatica.onrender.com/read_data/{turno}")

        if response.status_code == 200:
            return response.json()["values"]
        else:
            st.error("Desculpe, houve um erro no sistema, contacte os responsáveis.")
            return []
    except Exception as e:
        st.error(f"Erro: {e}")
        return []

# Função para desenhar a tabela
def draw_table(status, save_url, turno):

    data = fetch_sheet_data(turno)
    df = pd.DataFrame(data)
    if df.shape[1] == len(DIAS_DA_SEMANA):
        df.columns = DIAS_DA_SEMANA
    else:
        st.error("Número de colunas do DataFrame não corresponde aos dias da semana.")
        return

    # Gerar HTML da tabela
    thead1 = "<thead><tr><th style='background-color:#098aff;'scope='col'></th>"
    thead_temp = ["<th style='background-color:#098aff;'scope='col'>" + str(col) + "</th>" for col in df.columns]
    header = thead1 + "".join(thead_temp) + "</tr ></thead>"

    rows = ["<tr><th scope='row'></th>" for _ in range(df.shape[0])]
    cells = []
    for i, row in enumerate(df.values.tolist()):
        row_cells = []
        for j, value in enumerate(row):
            if str(value).lower() == 'livre':
                row_cells.append(
                    f"<td><button style='background-color:#1ef79399; color:black;' class='btn btn-success' onclick='openModal({i}, {j}, \"{df.columns[j]}\")'>{value}</button></td>")
            elif 'prof' in str(value).lower():
                row_cells.append(f"<td style='background-color:#e63946;'>{value}</td>")
            else:
                row_cells.append(f"<td style='background-color:#615EFC; color:white;'>{value}</td>")
        cells.append("".join(row_cells))

    body = "".join([rows[i] + cells[i] + "</tr>" for i in range(df.shape[0])])

    table_html = f"""
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
            <style>
                .table {{
                    border-collapse: collapse;
                    border: 1px solid #dee2e6;
                    box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
                }}
                .table th, .table td {{
                    border: 1px solid #dee2e6;
                    padding: 0.75rem;
                }}
                .table thead th {{
                    background-color: #007bff;
                    color: #fff;
                }}
                .table tbody td {{
                    background-color: #f8f9fa;
                }}
                .table tbody td.libre {{
                    background-color: #1ef79399;
                    color: #000;
                }}
                .table tbody td.professor {{
                    background-color: #ffc107;
                    color: #000;
                }}
                .table-responsive {{
                    max-width: 100%;
                    overflow-x: auto;
                }}
                .table {{
                    width: 100%;
                    max-width: 100%;
                    margin-bottom: 1rem;
                    text-align: center;
                }}
            </style>
            <script>
                function openModal(row, col, column) {{
                    var modal = new bootstrap.Modal(document.getElementById('editModal'));
                    document.getElementById('modalRow').value = row;
                    document.getElementById('modalCol').value = col;
                    document.getElementById('modalColumn').value = column;
                    document.getElementById('modalValue').value = document.querySelectorAll('tbody tr')[row].querySelectorAll('td')[col].textContent;
                    modal.show();
                }}
                function confirmSave() {{
                    var value = document.getElementById('modalValue').value;
                    if (value.trim() === "" || value.trim().toLowerCase() === "livre") {{
                        alert("O campo não pode estar vazio ou ser 'livre'!");
                        return;
                    }}
                    var confirmModal = new bootstrap.Modal(document.getElementById('confirmModal'));
                    confirmModal.show();
                }}
                function saveValue() {{
                    var row = document.getElementById('modalRow').value;
                    var col = document.getElementById('modalCol').value;
                    var column = document.getElementById('modalColumn').value;
                    var value = document.getElementById('modalValue').value;
                    if (value.trim() === "" || value.trim().toLowerCase() === "livre") {{
                        alert("O campo não pode estar vazio ou ser 'livre'!");
                        return;
                    }}
                    var displayValue = "Prof: " + value;
                    document.querySelectorAll('tbody tr')[row].querySelectorAll('td')[col].innerHTML = displayValue;
                    updateDataFrame(row, column, displayValue);
                }}
                function updateDataFrame(row, column, value) {{
                    var df = {df.to_json(orient='split')};
                    df.data[row][df.columns.indexOf(column)] = value;
                    saveDataToJSON(df);
                }}
                function saveDataToJSON(df) {{
                   fetch('{save_url}', {{
                        method: 'POST',
                        headers: {{
                            'Content-Type': 'application/json'
                        }},
                        body: JSON.stringify(df.data.map(row => {{
                            let obj = {{}};
                            df.columns.forEach((col, idx) => {{
                                obj[col] = row[idx];
                            }});
                            return obj;
                        }}))
                    }})
                    .then(response => {{
                    
                        if (response.ok) {{
                            console.log('Data saved successfully!');
                            var editModal = bootstrap.Modal.getInstance(document.getElementById('editModal'));
                            var confirmModal = bootstrap.Modal.getInstance(document.getElementById('confirmModal'));
                            editModal.hide();
                            confirmModal.hide();
                           
                        }} else {{
                            console.error('Error saving data:', response.status);
                        }}
                    }})
                    .catch(error => {{
                        console.error('Error saving data:', error);
                    }});
                }}
                
               // Armazena uma cópia do DataFrame original
                var originalDF = JSON.parse(`{df.to_json(orient='split')}`);
                
                function updateDataFrame(row, column, value) {{
                    // Atualiza o valor no DataFrame global
                    originalDF.data[row][originalDF.columns.indexOf(column)] = value;
                    saveDataToJSON(originalDF);

                    
                    // Armazena uma referência direta para o elemento da célula
                    var cellElement = document.querySelectorAll('tbody tr')[row].querySelectorAll('td')[column];
                    cellElement.textContent = value;
                }}

            </script>
            <div class="table-responsive">
                <table class="table table-bordered table-sm text-center">
                    {header}
                    <tbody>
                        {body}
                    </tbody>
                </table>
            </div>
            <div class="modal fade" id="editModal" tabindex="-1" aria-labelledby="editModalLabel" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="editModalLabel">Nome do professor</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body">
                            <input type="hidden" id="modalRow">
                            <input type="hidden" id="modalCol">
                            <input type="hidden" id="modalColumn">
                            <div class="mb-3">
                                <label for="modalValue" class="form-label">Digite apenas seu nome.</label>
                                <label for="modalValue" class="form-label-one">Antes de salvar, verifique se o turno está correto.</label>
                                <input type="text" class="form-control" id="modalValue">
                            </div>
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Fechar</button>
                            <button type="button" class="btn btn-primary" onclick="confirmSave()">Salvar</button>
                        </div>
                    </div>
                </div>
            </div>
            <div class="modal fade" id="confirmModal" tabindex="-1" aria-labelledby="confirmModalLabel" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="confirmModalLabel">Confirmar Salvar</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body">
                            <p>Tem certeza que deseja salvar as alterações?</p>
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
                            <button type="button" class="btn btn-primary" onclick="saveValue()">Confirmar</button>
                        </div>
                    </div>
                </div>
            </div>
            """

    # Exibir tabela
    components.html(table_html, height=600, scrolling=True)

