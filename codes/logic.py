import os
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Defina as permissões necessárias
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

def authenticate():
    creds = None

    # Obter o caminho absoluto do arquivo token.json
    token_file = os.path.join(os.path.dirname(__file__), "token.json")

    # Carregar as credenciais do arquivo token.json se existir
    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file, SCOPES)
    # Se não houver credenciais válidas disponíveis, solicita que o usuário faça login
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "client_secret.json", SCOPES
            )
            creds = flow.run_local_server(port=0)

        # Salvar as credenciais para a próxima execução
        with open(token_file, "w") as token:
            token.write(creds.to_json())

    return creds

def read_sheet(service, spreadsheet_id, range_name):
    try:
        request = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueRenderOption="UNFORMATTED_VALUE",
            majorDimension="ROWS"
        )
        response = request.execute()
        return response.get("values", [])
    except Exception as e:
        print(f"Erro ao ler a planilha {spreadsheet_id}: {e}")
        return []

def write_sheet(service, spreadsheet_id, range_name, values):
    try:
        body = {
            "values": values
        }
        result = service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption="RAW",
            body=body
        ).execute()
        return result
    except Exception as e:
        print(f"Erro ao escrever na planilha {spreadsheet_id}: {e}")

def main():
    creds = authenticate()
    service = build("sheets", "v4", credentials=creds)

    # IDs das planilhas de origem e destino
    source_sheet_id = "1B-T7GZTlzpdCuk9Ve37mjgf2pKNg2CmgG02lm5GvBZg"  # Planilha de origem
    target_sheet_id = "1B-T7GZTlzpdCuk9Ve37mjgf2pKNg2CmgG02lm5GvBZg"  # Planilha de destino

    # Intervalo da planilha de origem (considerando 9 colunas)
    source_range = "LAB DE MECANICA AUTOMOTIVA!B1:J100"  # Exemplo de intervalo

    # Lendo dados da planilha de origem
    source_data = read_sheet(service, source_sheet_id, source_range)
    if not source_data:
        print("Nenhum dado encontrado na planilha de origem.")
        return

    # Intervalo da planilha de destino (considerando 9 colunas)
    target_range = "LAB DE MECANICA AUTOMOTIVA!A3:I100"  # Exemplo de intervalo

    # Escrevendo dados na planilha de destino
    write_sheet(service, target_sheet_id, target_range, source_data)
    print("Dados escritos na planilha de destino.")

if __name__ == "__main__":
    main()
