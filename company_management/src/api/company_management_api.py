from fastapi import FastAPI
from services.company_management_service import (
    retrieve_all_companies,
    retrieve_company_by_id,
    create_company,
    update_company,
    remove_company
)
app = FastAPI()


@app.get("/companies/health")
def health_check():
    """Health check endpoint to verify the API is running."""
    return {"status": "Company Management API is running"}


@app.get("/companies/")
def get_all_companies():
    """Retrieve all companies."""
    return retrieve_all_companies()


@app.get("/companies/{company_id}")
def get_company_by_id(company_id: str):
    return retrieve_company_by_id(company_id)


@app.post("/companies/")
def post_company(company: dict):
    """Create a new company."""
    return create_company(company)


@app.put("/companies/{company_id}")
def put_company(company_id: str, company: dict):
    """Update an existing company by its ID."""
    return update_company(company_id, company)


@app.delete("/companies/{company_id}")
def delete_contact(company_id: str):
    """Remove a contact by its ID."""
    return remove_company(company_id)