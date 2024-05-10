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
    spreadsheet_id = "1D8Lrx73soJV6BblRmsHVFVuDjnGifPf2QZlGsMKeI0E"
    ranges = ["Respostas ao formulário 1!A:A", "Respostas ao formulário 1!C:C", "Respostas ao formulário 1!D:D", "Respostas ao formulário 1!P:P2"]

    # Chama a API Sheets para obter os valores dos intervalos especificados
    request = service.spreadsheets().values().batchGet(
        spreadsheetId=spreadsheet_id,
        ranges=ranges,
        valueRenderOption="UNFORMATTED_VALUE",
        majorDimension="COLUMNS"
    )
    response = request.execute()

    # Processa as respostas para cada intervalo
    for value_range in response["valueRanges"]:
        range_name = value_range["range"]
        values = value_range.get("values", [])

        if not values:
            print(f"No data found in range: {range_name}")
        else:

            for row in values:
                print(row)

if __name__ == "__main__":
    main()
