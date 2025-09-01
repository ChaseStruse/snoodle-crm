import uuid
from models.company_management_api_response import CompanyManagementAPIResponse
from models.company import Company
from repositories.company_management_repository import (
    get_all_companies
)

def convert_json_to_company(company_json: dict):
    return Company(
        id=uuid.uuid4(),
        name=company_json.get("name"),
        business_contact_email=company_json.get("businessContactEmail"),
        business_contact_phone_number=company_json.get("businessContactPhoneNumber"),
        address=company_json.get("address"),
        date_added=date.today(),
        primary_contact_id=company_json.get("primaryContactId")
    )

def retrieve_all_companies() -> dict:
    try:
        companies = get_all_companies()
        response_obj = CompanyManagementAPIResponse(company_id="all", data={ "companies": companies }, message="All companies retrieved successfully")
        return response_obj.response()
    except Exception as e:
        response_obj = CompanyManagementAPIResponse(company_id="Error", success=False, message=f"Error retrieving companies, please try again.")
        return response_obj.response()
    

def create_company(company: dict) -> dict:
    try:
        company_obj = convert_json_to_contact(contact)
        inserted_contact = insert_contact(contact=contact_obj)
        response_obj = ContactManagementAPIResponse(contact_id="123", data=inserted_contact.get_response_data(), message="Contact created successfully")

        return response_obj.response()
    except Exception as e:
        response_obj = ContactManagementAPIResponse(contact_id="Error", success=False, message=f"Error creating contact, please try again.")
        return response_obj.response()