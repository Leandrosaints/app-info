from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import logging

logging.basicConfig(level=logging.DEBUG)

app = FastAPI()

# Configure CORS
origins = [
    "http://localhost:8501",
    "http://192.168.0.106:8501"
    # Adicione mais URLs se necessário
]

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

@app.post("/save_data")
async def save_data(data: list[LabData]):
    try:
        logging.debug("Received data: %s", data)
        with open('files/data.json', 'w') as f:
            json.dump([item.dict() for item in data], f, indent=4)
        logging.debug("Data saved successfully!")
        return {"message": "Data saved successfully!"}
    except Exception as e:
        logging.error("Error saving data: %s", e)
        raise HTTPException(status_code=500, detail=str(e))

@app.options("/save_data")
async def options_save_data():
    return {}
