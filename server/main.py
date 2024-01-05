from fastapi import FastAPI
app = FastAPI()

@app.get('/api/data')
def data():
    data = {'message': 'Hello from the backend!'}
    return data
