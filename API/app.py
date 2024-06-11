"""from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
from logica import write_sheet, read_sheet

#logging.basicConfig(level=logging.DEBUG)

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


    # Chama a função de leitura
    values = read_sheet()
    return {"values": values}

if __name__ == "__main__":
    app.run(debug=True)"""
from urllib import request

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import logging

from pydantic import BaseModel

from logica import write_sheet, read_sheet
import threading

app = FastAPI()

# Configurar CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LabData(BaseModel):
    LAB: str
    Seg: str
    Ter: str
    Qua: str
    Qui: str
    Sex: str

# Criar uma trava global
write_lock = threading.Lock()

@app.post("/write_data/{turno}")
async def write_data(data: list[LabData], turno):
    # Adquirir a trava antes de escrever na planilha
    write_lock.acquire()
    try:
        logging.debug("Received data: %s", data)
        write_sheet([item.dict() for item in data], turno)
        logging.debug("Data saved successfully!")
        return {"message": "Data saved successfully!"}
    finally:
        # Liberar a trava após a operação ser concluída
        write_lock.release()

@app.get("/read_data/{turno}")
async def read_data(turno):
    # Chama a função de leitura
    values = read_sheet(turno)
    return {"values": values}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8080)

