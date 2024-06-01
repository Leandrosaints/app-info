import os
import streamlit as st
import json
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Carregar variáveis de ambiente do arquivo .env
from dotenv import load_dotenv
load_dotenv()

# Obter o caminho dos arquivos do ambiente
CLIENT_SECRET_PATH = os.getenv('CLIENT_SECRET_PATH')

SCOPES = ['openid', 'https://www.googleapis.com/auth/userinfo.profile',
          'https://www.googleapis.com/auth/userinfo.email']

def get_cookie(name):
    if name in st.session_state:
        try:
            return json.loads(st.session_state[name])
        except (json.JSONDecodeError, TypeError):
            pass
    return None

def set_cookie(name, value):
    st.session_state[name] = json.dumps(value)

def autenticar_usuario():
    creds = None

    # Tentar carregar as credenciais do cache do Streamlit
    if 'credentials' in st.session_state:
        creds = Credentials.from_authorized_user_info(st.session_state['credentials'])
    # Tentar carregar as credenciais dos cookies
    elif get_cookie('credentials'):
        creds_info = get_cookie('credentials')
        creds = Credentials(
            token=creds_info['token'],
            refresh_token=creds_info['refresh_token'],
            client_id=creds_info['client_id'],
            client_secret=creds_info['client_secret'],
            scopes=SCOPES
        )

    # Se não houver credenciais válidas disponíveis, solicita que o usuário faça login
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            CLIENT_SECRET_PATH, SCOPES
        )

        creds = flow.run_local_server(port=0)

        # Salvar as credenciais no cache do Streamlit
        st.session_state['credentials'] = creds.to_json()
        # Salvar as credenciais nos cookies
        set_cookie('credentials', {
            'token': creds.token,
            'refresh_token': creds.refresh_token,
            'client_id': creds.client_id,
            'client_secret': creds.client_secret
        })

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
