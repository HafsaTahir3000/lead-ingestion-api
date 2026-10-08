from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
from datetime import datetime


class Lead(BaseModel):
    name: str
    email: str
    phone: str
    source: str

conn = sqlite3.connect("leads.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS leads (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    phone TEXT,
    source TEXT,
    created_at TEXT
)
""")

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Lead Ingestion API is running"}


@app.post("/leads", status_code=201)
def create_lead(lead: Lead):
    created_at = datetime.now().isoformat()

    cursor.execute(
        "INSERT INTO leads (name, email, phone, source, created_at) VALUES (?, ?, ?, ?, ?)",
        (lead.name, lead.email, lead.phone, lead.source, created_at)
    )
    conn.commit()
    return lead

@app.get("/leads")
def get_leads():
    cursor.execute("SELECT * FROM leads")
    rows = cursor.fetchall()
    leads = []

    for row in rows:
        lead = {}
        lead["id"] = row[0]
        lead["name"] = row[1]
        lead["email"] = row[2]
        lead["phone"] = row[3]
        lead["source"] = row[4]
        lead["created_at"] = row[5]
        leads.append(lead)

    return leads