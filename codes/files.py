classroom_items = [
    "Projetor funcionando",
    "Ar condicionado funcionando",
    "Computador funcionando",
    "Iluminação adequada",
    "Quadro branco disponível",
]

links = [
    {"text": "home", "url": "#", "icon": "fa-sharp fa-solid fa-house"},
    {"text": "form Salas", "url": "https://forms.gle/6eUoZDu63GjgML169","icon": "fa-solid fa-list-check"},
    {"text": "form Labs", "url": "https://forms.gle/JHXVPmYh3TWfbcs96","icon": "fa-solid fa-desktop"}
]



"""json_data = '''
{
    "laboratorio 01": {
        "nome": "Laboratorio 01",
        "N_maquinas": 30,
        "softweres_instalados": ["office 365", "Fusion", "arduino", "lego", "chrome", "chrome"]
    },
    "laboratorio 02": {
        "nome": "Laboratorio 02",
        "N_maquinas": 25,
        "softweres_instalados": ["office 365", "Visual Studio Code", "Arduino IDE", "Anaconda Navigator"]
    }
}
'''"""
import json

# Defina os valores das variáveis
laboratorio_01 = {
    "nome": "Laboratorio 01",
    "N_maquinas": 30,
    "softweres_instalados": ["office 365", "Fusion", "arduino", "lego", "chrome", "chrome"]
}

laboratorio_02 = {
    "nome": "Laboratorio 02",
    "N_maquinas": 25,
    "softweres_instalados": ["office 365", "Visual Studio Code", "Arduino IDE", "Anaconda Navigator"]
}

# Crie um dicionário principal que inclui os laboratórios
json_data = {
    "laboratorio 01": laboratorio_01,
    "laboratorio 02": laboratorio_02
}

# Converta o dicionário em uma string JSON
json_string = json.dumps(json_data, indent=4)

# Agora você pode usar a variável json_string conforme necessário em seu código
