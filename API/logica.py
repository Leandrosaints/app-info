import os
from dotenv import load_dotenv
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Defina as permissões necessárias
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
# Carregar variáveis de ambiente do arquivo .env
load_dotenv(dotenv_path='.env')

# Obter o caminho dos arquivos do ambiente
CLIENT_SECRET_PATH = os.getenv('CLIENT_SECRET_PATH')
TOKEN_PATH = os.getenv('TOKEN_PATH')

def authenticate():
    creds = None

    # Carregar as credenciais do arquivo token.json se existir
    if TOKEN_PATH and os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    # Se não houver credenciais válidas disponíveis, solicita que o usuário faça login
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if CLIENT_SECRET_PATH and os.path.exists(CLIENT_SECRET_PATH):
                flow = InstalledAppFlow.from_client_secrets_file(
                    CLIENT_SECRET_PATH, SCOPES
                )
                creds = flow.run_local_server(port=0)
            else:
                raise ValueError("O caminho do arquivo 'client_secret.json' não está definido corretamente.")

        # Salvar as credenciais para a próxima execução
        if TOKEN_PATH:
            with open(TOKEN_PATH, "w") as token:
                token.write(creds.to_json())

    return creds


# Restante do código permanece o mesmo...


def write_sheet(values, turno):
    creds = authenticate()
    service = build("sheets", "v4", credentials=creds, cache_discovery=False)
    values_list = [[item['LAB'], item['Seg'], item['Ter'], item['Qua'], item['Qui'], item['Sex']] for item in values]


    body = {
        "values": values_list
    }
    result = service.spreadsheets().values().update(
        spreadsheetId='1SckA6j63wLa17J-7wstwL-rA8tN5sKxDBnlfBsJcOk8',
        range=f"{turno}!A2:F8",
        valueInputOption="RAW",
        body=body
    ).execute()
    return result


def read_sheet(turno):
    creds = authenticate()
    service = build("sheets", "v4", credentials=creds)

    try:
        request = service.spreadsheets().values().get(
            spreadsheetId='1SckA6j63wLa17J-7wstwL-rA8tN5sKxDBnlfBsJcOk8',
            range=f"{turno}!A2:F8",
            valueRenderOption="UNFORMATTED_VALUE",
            majorDimension="ROWS"
        )
        response = request.execute()

        return response.get("values", [])

    except Exception as e:
        print(f"Erro ao ler a planilha  {e}")
        return []


