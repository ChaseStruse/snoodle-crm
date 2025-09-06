from fastapi import FastAPI
from utils.logger import setup_logger
from services.company_management_service import (
    retrieve_all_companies,
    retrieve_company_by_id,
    create_company,
    update_company,
    remove_company
)
app = FastAPI()

logger = setup_logger(__name__)

@app.get("/companies/health")
def health_check():
    """Health check endpoint to verify the API is running."""
    logger.info("Health check endpoint called")
    return {"status": "Company Management API is running"}


@app.get("/companies/")
def get_all_companies():
    """Retrieve all companies."""
    logger.info("Retrieving all companies")
    return retrieve_all_companies()


@app.get("/companies/{company_id}")
def get_company_by_id(company_id: str):
    logger.info(f"Retrieving company with ID: {company_id}")
    return retrieve_company_by_id(company_id)


@app.post("/companies/")
def post_company(company: dict):
    """Create a new company."""
    logger.info("Creating a new company")
    return create_company(company)


@app.put("/companies/{company_id}")
def put_company(company_id: str, company: dict):
    """Update an existing company by its ID."""
    logger.info(f"Updating company with ID: {company_id}")
    return update_company(company_id, company)


@app.delete("/companies/{company_id}")
def delete_contact(company_id: str):
    """Remove a contact by its ID."""
    logger.info(f"Removing company with ID: {company_id}")
    return remove_company(company_id)