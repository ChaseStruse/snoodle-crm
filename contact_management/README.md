# Contact Management Module

This module provides a FastAPI-based RESTful API for managing contacts in a CRM system. It uses SQLite as the database backend and SQLAlchemy for ORM.

## Features

- Create, retrieve, update, and delete contacts
- Health check endpoint
- SQLite database integration via SQLAlchemy
- Modular repository and service layers

## Folder Structure

```
contact_management/
├── src/
│   ├── api/
│   │   └── contact_management_api.py
│   ├── models/
│   │   └── contact.py
│   ├── repositories/
│   │   └── contact_management_repository.py
│   ├── services/
│   │   └── contact_management_service.py
│   └── db.py
├── contacts.db
└── README.md
```

## Setup

1. **Install dependencies:**
   ```sh
   pip install fastapi sqlalchemy aiosqlite uvicorn
   ```

2. **Create the database tables:**
   ```sh
   PYTHONPATH=src python src/db.py
   ```
   *(Make sure `create_tables()` is called in `db.py`)*

3. **Run the API server:**
   ```sh
   make run-contact
   ```

## API Endpoints

- `GET /contacts/health` — Health check
- `GET /contacts/` — Retrieve all contacts
- `GET /contacts/{contact_id}` — Retrieve a contact by ID
- `POST /contacts/` — Create a new contact
- `PUT /contacts/{contact_id}` — Update a contact
- `DELETE /contacts/{contact_id}` — Delete a contact

## Example Contact Object

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "phoneNumber": "123-456-7890",
  "address": "123 Main St",
  "dateOfBirth": "1990-01-01"
}
```