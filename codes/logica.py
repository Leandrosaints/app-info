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

def write_sheet(values):
    creds = authenticate()
    service = build("sheets", "v4", credentials=creds)
    values_list = [[item['LAB'], item['Seg'], item['Ter'], item['Qua'], item['Qui'], item['Sex']] for item in values]

    try:
        body = {
            "values": values_list
        }
        result = service.spreadsheets().values().update(
            spreadsheetId='1SckA6j63wLa17J-7wstwL-rA8tN5sKxDBnlfBsJcOk8',
            range="agendamentos de laboratorios!B2:F8",
            valueInputOption="RAW",
            body=body
        ).execute()
        return result
    except Exception as e:
        print(f"Erro ao escrever na planilha 1SckA6j63wLa17J-7wstwL-rA8tN5sKxDBnlfBsJcOk8: {e}")
        return None

def read_sheet():
    creds = authenticate()
    service = build("sheets", "v4", credentials=creds)

    try:
        request = service.spreadsheets().values().get(
            spreadsheetId='1SckA6j63wLa17J-7wstwL-rA8tN5sKxDBnlfBsJcOk8',
            range="agendamentos de laboratorios!A2:F8",
            valueRenderOption="UNFORMATTED_VALUE",
            majorDimension="ROWS"
        )
        response = request.execute()

        return response.get("values", [])

    except Exception as e:
        print(f"Erro ao ler a planilha  {e}")
        return []


