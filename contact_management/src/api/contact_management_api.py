from fastapi import FastAPI
from services.contact_management_service import (
    retrieve_all_contacts,
    retrieve_contact_by_id,
    create_contact,
    update_contact,
    remove_contact
)

app = FastAPI()

@app.get("/contacts/health")
def health_check():
    """Health check endpoint to verify the API is running."""
    return {"status": "Contact Management API is running"}

@app.get("/contacts/")
def get_all_contacts():
    """Retrieve all contacts."""
    return retrieve_all_contacts()

@app.get("/contacts/{contact_id}")
def get_contact(contact_id: str):
    """Retrieve a contact by its ID."""
    return retrieve_contact_by_id(contact_id)

@app.post("/contacts/")
def post_contact(contact: dict):
    """Create a new contact."""
    return create_contact(contact)

@app.put("/contacts/{contact_id}")
def put_contact(contact_id: str, contact: dict):
    """Update an existing contact by its ID."""
    return update_contact(contact_id, contact)

@app.delete("/contacts/{contact_id}")
def delete_contact(contact_id: str):
    """Remove a contact by its ID."""
    return remove_contact(contact_id)