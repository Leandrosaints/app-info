import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, DataReturnMode

# Carregando os dados
df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})

# Criando o GridOptionsBuilder
gb = GridOptionsBuilder.from_dataframe(df)

# Configurando colunas específicas para serem editáveis
gb.configure_column("col1", editable=True)
gb.configure_column("col2", editable=True)

# Construindo as opções de grade
gridOptions = gb.build()

# Criando o AgGrid com as opções de grade
response = AgGrid(
    df,
    gridOptions=gridOptions,
    height=600,
    width='100%',
    data_return_mode=DataReturnMode._NONE_,
    update_mode=GridUpdateMode._NONE_,
    fit_columns_on_grid_load=True,
    allow_unsafe_jscode=True,  # Permitir código JS inseguro
)

# Código JS para permitir/negar edição com base no valor da célula
js_code = """
function(e) {
    var cellValue = e.data[e.colDef.field];
    if (cellValue == 2) {
        e.columnApi.getColumn(e.colDef.field).colDef.editable = false;
    } else {
        e.columnApi.getColumn(e.colDef.field).colDef.editable = true;
    }
}
"""

# Adicionando o código JS ao evento de clique na célula
response['gridOptions']['onCellClicked'] = js_code