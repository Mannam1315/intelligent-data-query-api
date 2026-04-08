from fastapi import FastAPI
from rag.query_engine import query_data

app = FastAPI(title="Intelligent Data Query API")

@app.get("/")
def home():
    return {"message": "API is running"}

@app.get("/query")
def query(q: str):
    result = query_data(q)
    return {"question": q, "response": result}
