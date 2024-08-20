### uvicorn main:app --reload --host 0.0.0.0 --port 5000

from fastapi import FastAPI
from typing import List
from crud import fetch_all_data, insert_data
from module import Troops, TroopsTemplate, UserStrategy, UserTroops

app = FastAPI()


@app.get("/api/data", response_model=List[TroopsTemplate])
def read_data():
    data = fetch_all_data("troops_template")
    return data


@app.post("/api/post")
def post_data(data: TroopsTemplate):
    print('data', data)
    insert_data(data, "user_troops")
    msg = {"msg": "success"}
    return msg
