import requests

def recebe_dados(url):
    # Fazer a solicitação GET para a rota
    response = requests.get(url)

    # Verificar se a solicitação foi bem-sucedida e retornar os dados
    if response.status_code == 200:
        return response.json()
    else:
        print("Erro ao receber os dados:", response.status_code)
        return None

# Exemplo de uso
url = "http://192.168.0.106:8501/save_data"
dados_recebidos = recebe_dados(url)
if dados_recebidos is not None:
    print("Dados recebidos:", dados_recebidos)