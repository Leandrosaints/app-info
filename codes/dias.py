import json
from datetime import datetime, timedelta

def reset_past_days_to_free(json_data, last_update):
    current_day = datetime.now().strftime('%A')[:3]  # Obtém o dia da semana atual abreviado (Seg, Ter, Qua, Qui, Sex)

    # Calcula a diferença em dias entre o último reset e a data atual
    days_diff = (datetime.now() - last_update).days

    if days_diff > 0:
        for entry in json_data:
            for day, value in entry.items():
                if day in ['Seg', 'Ter', 'Qua', 'Qui', 'Sex']:
                    # Define o dia como "Livre" se estiver no passado em relação ao último reset
                    if days_diff >= {'Seg': 1, 'Ter': 2, 'Qua': 3, 'Qui': 4, 'Sex': 5}[day]:
                        entry[day] = "Livre"

    # Retorna a data e hora atuais após a atualização
    return datetime.now()

def load_last_update():
    try:
        with open('../files/last_update.txt', 'r') as f:
            last_update = datetime.fromisoformat(f.read())
    except FileNotFoundError:
        # Se o arquivo não existir, definimos a data de última atualização como uma semana atrás
        last_update = datetime.now() - timedelta(days=7)
    return last_update

def save_last_update(last_update):
    with open('../files/last_update.txt', 'w') as f:
        f.write(last_update.isoformat())

# Carregar a última data de atualização
last_update = load_last_update()

try:
    with open('../files/data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
except FileNotFoundError:
    # Se o arquivo não existir, criamos um arquivo vazio
    data = []
    with open('../files/data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

# Verifica se houve mudança de dia desde o último reset
if datetime.now().date() != last_update.date():
    last_update = reset_past_days_to_free(data, last_update)

    # Salvar os dados atualizados no arquivo JSON
    with open('../files/data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

    # Salvar a nova data de atualização
    save_last_update(last_update)

print("JSON salvo com sucesso.")
