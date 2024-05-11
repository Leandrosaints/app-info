import json
import os.path
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Defina as permissões necessárias
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]


def main():
    creds = None

    # Carrega as credenciais do arquivo token.json se existir
    if os.path.exists("client.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # Se não houver credenciais válidas disponíveis, solicita que o usuário faça login
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "token.json", SCOPES
            )
            creds = flow.run_local_server(port=0)

        # Salva as credenciais para a próxima execução
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    # Constrói o serviço Sheets
    service = build("sheets", "v4", credentials=creds)

    # ID da planilha e intervalos
    spreadsheet_id = "1Tk5U-uDoguGsmyMdIqFimDoz4W8opgsxtHbw8EQrvUw"
    ranges = ["Respostas ao formulário 1!A:N"]

    # Chama a API Sheets para obter os valores dos intervalos especificados
    request = service.spreadsheets().values().batchGet(
        spreadsheetId=spreadsheet_id,
        ranges=ranges,
        valueRenderOption="UNFORMATTED_VALUE",
        majorDimension="COLUMNS"
    )
    response = request.execute()

    # Processa as respostas para cada intervalo
    lab_data_dict = {}
    for value_range in response["valueRanges"]:
        values = value_range.get("values", [])

        if not values:
            print(f"No data found in range")
        else:
            # Itera sobre os valores para extrair os dados de cada laboratório
            for row in range(1, len(values[0])):  # Começa a partir da segunda linha (a primeira linha contém os cabeçalhos)
                lab_name = values[2][row]  # Nome do laboratório na coluna C
                lab_data = {
                    "nome": values[2][row],  # Nome do laboratório
                    "N_maquinas": int(values[3][row]),  # Número de máquinas (convertido para inteiro)
                    "softweres_instalados": values[6][row].split(", ")  # Softwares instalados
                }
                lab_data_dict[f"laboratorio_{row}"] = lab_data

    # Salva os dados em um arquivo JSON
    with open("output.json", "w") as json_file:
        json.dump(lab_data_dict, json_file, indent=4)


if __name__ == "__main__":
    main()
