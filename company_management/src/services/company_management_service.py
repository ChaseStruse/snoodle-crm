import uuid
from datetime import date
from models.company_management_api_response import CompanyManagementAPIResponse
from models.company import Company
from repositories.company_management_repository import (
    get_all_companies,
    get_company_by_id,
    insert_company
)

def convert_json_to_company(company_json: dict):
    return Company(
        id=uuid.uuid4(),
        name=company_json.get("name"),
        business_contact_email=company_json.get("businessContactEmail"),
        business_contact_phone_number=company_json.get("businessContactPhoneNumber"),
        address=company_json.get("address"),
        date_added=date.today(),
        primary_contact_id=uuid.UUID(company_json.get("primaryContactId"))
    )

def retrieve_all_companies() -> dict:
    try:
        companies = get_all_companies()
        response_obj = CompanyManagementAPIResponse(company_id="all", data={ "companies": companies }, message="All companies retrieved successfully")
        return response_obj.response()
    except Exception as e:
        response_obj = CompanyManagementAPIResponse(company_id="Error", success=False, message=f"Error retrieving companies, please try again.")
        return response_obj.response()
    

def retrieve_company_by_id(company_id: str) -> dict:
    try:
        company = get_company_by_id(company_id=uuid.UUID(company_id))
        if company:
            response_obj = CompanyManagementAPIResponse(company_id=company_id, data=company.get_response_data(), message="Company retrieved successfully")
        else:
            response_obj = CompanyManagementAPIResponse(company_id=company_id, success=False, message="Company not found")
        return response_obj.response()
    except Exception as e:
        response_obj = CompanyManagementAPIResponse(company_id=company_id, success=False, message=f"Error retrieving company, please try again.")
        return response_obj.response()
    

def create_company(company: dict) -> dict:
    try:
        company_obj = convert_json_to_company(company)
        inserted_company = insert_company(company=company_obj)
        response_obj = CompanyManagementAPIResponse(company_id=str(company_obj.id), data=inserted_company.get_response_data(), message="Company created successfully")

        return response_obj.response()
    except Exception as e:
        response_obj = CompanyManagementAPIResponse(company_id="Error", success=False, message=f"Error creating company, please try again.")
        return response_obj.response()