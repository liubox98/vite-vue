### uvicorn main:app --reload --host 0.0.0.0 --port 5000

from fastapi import FastAPI

app = FastAPI()


@app.get("/api/data")
def data():
    data = [
        {
            "mingcheng": "guanyu",
            "bingzhong": 123,
            "dengji": 10,
            "zhujiang": "123",
            "jineng1": "wqer",
            "jineng2": "qwer",
            "fujiang1": "123",
            "jineng1": "wqer",
            "jineng2": "qwer",
            "fujiang2": "123",
            "jineng1": "wqer",
            "jineng2": "qwer",
        },
        {
            "mingcheng": "nihao",
            "bingzhong": 123,
            "dengji": 10,
            "zhujiang": "123",
            "jineng1": "wqer",
            "jineng2": "qwer",
            "fujiang1": "123",
            "jineng1": "wqer",
            "jineng2": "qwer",
            "fujiang2": "123",
            "jineng1": "wqer",
            "jineng2": "qwer",
        },
        {
            "mingcheng": "nihao",
            "bingzhong": 123,
            "dengji": 10,
            "zhujiang": "123",
            "jineng1": "wqer",
            "jineng2": "qwer",
            "fujiang1": "123",
            "jineng1": "wqer",
            "jineng2": "qwer",
            "fujiang2": "123",
            "jineng1": "wqer",
            "jineng2": "qwer",
        },
    ]
    return data
