import os
import streamlit as st
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter o caminho dos arquivos do ambiente
CLIENT_SECRET_PATH = os.getenv('CLIENT_SECRET_PATH')
TOKEN_PATH = os.getenv('TOKEN_PATH')

SCOPES = ['openid', 'https://www.googleapis.com/auth/userinfo.profile',
          'https://www.googleapis.com/auth/userinfo.email']


def autenticar_usuario():
    creds = None

    # Carregar as credenciais do arquivo token.json se existir
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)

    # Se não houver credenciais válidas disponíveis, solicita que o usuário faça login
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            CLIENT_SECRET_PATH, SCOPES
        )
        creds = flow.run_local_server(port=0)

        # Salvar as credenciais para a próxima execução
        with open(TOKEN_PATH, "w") as token:
            token.write(creds.to_json())

    # Obter as informações do usuário usando a API do Google People
    people_api = build('people', 'v1', credentials=creds)
    user_info = people_api.people().get(
        resourceName='people/me',
        personFields='emailAddresses,names'
    ).execute()

    return {
        'email': user_info['emailAddresses'][0]['value'],
        'name': user_info['names'][0]['displayName']
    }


def handle_authentication():
    user_info = autenticar_usuario()
    return user_info



