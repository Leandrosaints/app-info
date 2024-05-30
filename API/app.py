from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
from API.logica import write_sheet, read_sheet

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
CORS(app)
class LabData:
    def __init__(self, LAB, Seg, Ter, Qua, Qui, Sex):
        self.LAB = LAB
        self.Seg = Seg
        self.Ter = Ter
        self.Qua = Qua
        self.Qui = Qui
        self.Sex = Sex

    def to_dict(self):
        return {
            "LAB": self.LAB,
            "Seg": self.Seg,
            "Ter": self.Ter,
            "Qua": self.Qua,
            "Qui": self.Qui,
            "Sex": self.Sex
        }
import threading

# Criar uma trava global
write_lock = threading.Lock()

@app.route("/write_data", methods=["POST"])
def write_data():
    # Adquirir a trava antes de escrever na planilha
    write_lock.acquire()

    try:
        if request.method == "OPTIONS":
            return jsonify({})

        data = request.get_json()
        lab_data_list = [LabData(**item) for item in data]
        logging.debug("Received data: %s", lab_data_list)
        write_sheet([item.to_dict() for item in lab_data_list])
        logging.debug("Data saved successfully!")
        return jsonify({"message": "Data saved successfully!"})

    finally:
        # Liberar a trava após a operação ser concluída
        write_lock.release()

# Recebe os dados a serem escritos na planilha
#data = request.get_json()

#values = data["values"]

# Chama a função de escrita
#write_sheet(values)


@app.route("/read_data", methods=["GET"])
def read_data():
    # Recebe os parâmetros para leitura da planilha
    spreadsheet_id = request.args.get("spreadsheet_id")
    range_name = request.args.get("range_name")

    # Chama a função de leitura
    values = read_sheet()
    return {"values": values}

if __name__ == "__main__":
    app.run(debug=True)
