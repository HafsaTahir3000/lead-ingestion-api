from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Lead Ingestion API is running"}