# Lead Ingestion API

A REST API built with Python, FastAPI, Pydantic, and SQLite to collect, validate, store, and retrieve customer leads.

## Features

- Accept new leads through POST /leads
- Validate required fields using Pydantic
- Store leads in a SQLite database
- Retrieve saved leads through GET /leads
- Record timestamps for new leads
- Use parameterized SQL queries for safer database operations

## Technologies

Python, FastAPI, Pydantic, SQLite, Uvicorn

## Run Locally

1. Create a virtual environment: python3 -m venv .venv
2. Activate: source .venv/bin/activate
3. Install: pip install fastapi uvicorn
4. Start: uvicorn main:app --reload
5. Open: http://127.0.0.1:8000/docs

The database file is created automatically.

## API Endpoints

GET / — Health check
POST /leads — Create a lead
GET /leads — Retrieve all leads

## Example Request

{
  "name": "Sara",
  "email": "sara@example.com",
  "phone": "5715552222",
  "source": "Website"
}

## Future Improvements

Email validation, lead analytics, authentication, automated tests.