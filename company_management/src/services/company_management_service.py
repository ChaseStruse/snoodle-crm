import uuid
from utils.logger import setup_logger
from datetime import date
from models.company_management_api_response import CompanyManagementAPIResponse
from models.company import Company
from repositories.company_management_repository import (
    get_all_companies,
    get_company_by_id,
    insert_company,
    update_company_by_id,
    remove_company_by_id
)

logger = setup_logger(__name__)

def convert_json_to_company(company_json: dict, company_id=uuid.uuid4()) -> Company:
    logger.info("Converting passed in JSON to Company object")

    try:
       return Company(
            id=company_id,
            name=company_json.get("name"),
            business_contact_email=company_json.get("businessContactEmail"),
            business_contact_phone_number=company_json.get("businessContactPhoneNumber"),
            address=company_json.get("address"),
            date_added=date.today(),
            primary_contact_id=uuid.UUID(company_json.get("primaryContactId"))
        )
    except Exception as e:
        logger.error(f"Error converting JSON to Company object: {e}")
        raise
     

def retrieve_all_companies() -> dict:
    try:
        companies = get_all_companies()
        response_obj = CompanyManagementAPIResponse(company_id="all", data={ "companies": companies }, message="All companies retrieved successfully")
        logger.info("Finished retrieving all companies, status: success.")
        return response_obj.response()
    except Exception as e:
        response_obj = CompanyManagementAPIResponse(company_id="Error", success=False, message=f"Error retrieving companies, please try again.")
        logger.error(f"Error retrieving all companies: {e}")
        return response_obj.response()
    

def retrieve_company_by_id(company_id: str) -> dict:
    try:
        company = get_company_by_id(company_id=uuid.UUID(company_id))
        if company:
            logger.info(f"Company with ID: {company_id} found.")
            response_obj = CompanyManagementAPIResponse(company_id=company_id, data=company.get_response_data(), message="Company retrieved successfully")
        else:
            logger.warning(f"Company with ID: {company_id} not found.")
            response_obj = CompanyManagementAPIResponse(company_id=company_id, success=False, message="Company not found")
        return response_obj.response()
    except Exception as e:
        logger.error(f"Error retrieving company with ID: {company_id}: {e}")
        response_obj = CompanyManagementAPIResponse(company_id=company_id, success=False, message=f"Error retrieving company, please try again.")
        return response_obj.response()
    

def create_company(company: dict) -> dict:
    try:
        company_obj = convert_json_to_company(company)
        inserted_company = insert_company(company=company_obj)
        response_obj = CompanyManagementAPIResponse(company_id=str(company_obj.id), data=inserted_company.get_response_data(), message="Company created successfully")
        logger.info(f"Company with ID: {company_obj.id} created successfully.")
        return response_obj.response()
    except Exception as e:
        logger.error(f"Error creating company: {e}")
        response_obj = CompanyManagementAPIResponse(company_id="Error", success=False, message=f"Error creating company, please try again.")
        return response_obj.response()
    

def update_company(company_id: str, company: dict) -> dict:
    try:
        company_obj = convert_json_to_company(company, company_id=uuid.UUID(company_id))
        updated_company = update_company_by_id(company_id=uuid.UUID(company_id), company=company_obj)
        response_obj = CompanyManagementAPIResponse(company_id=company_id, data=updated_company.get_response_data(),
                                                    message="Company updated successfully")
        logger.info(f"Company with ID: {company_id} updated successfully.")
        return response_obj.response()
    except Exception as e:
        logger.error(f"Error updating company with ID: {company_id}: {e}")
        response_obj = CompanyManagementAPIResponse(company_id=company_id, success=False, message=f"Error updating company, please try again.")
        return response_obj.response()


def remove_company(company_id: str) -> dict:
    try:
        remove_company_by_id(company_id=uuid.UUID(company_id))
        response_obj = CompanyManagementAPIResponse(company_id=company_id, message="Company removed successfully")
        logger.info(f"Company with ID: {company_id} removed successfully.")
        return response_obj.response()
    except Exception as e:
        logger.error(f"Error removing company with ID: {company_id}: {e}")
        response_obj = CompanyManagementAPIResponse(company_id=company_id, success=False, message=f"Error removing company, please try again.")
        return response_obj.response()