import uuid
from responses.contact_management_api_response import ContactManagementAPIResponse
from repositories.contact_management_repository import (
    insert_contact,
    get_all_contacts,
    get_contact_by_id,
    update_contact_by_id,
    remove_contact_by_id
)
from models.contact import Contact
from datetime import date, datetime

def convert_json_to_contact(contact_json: dict) -> Contact:
    date_of_birth_str = contact_json.get("dateOfBirth")
    if date_of_birth_str:
        date_of_birth = datetime.strptime(date_of_birth_str, "%Y-%m-%d").date()
    else:
        date_of_birth = None

    return Contact(
        id=uuid.uuid4(),
        name=contact_json.get("name"),
        email=contact_json.get("email"),
        phone_number=contact_json.get("phoneNumber"),
        address=contact_json.get("address"),
        date_of_birth=date_of_birth,
        date_added=date.today(),
        last_contacted=date.today()
    )

def retrieve_all_contacts() -> dict:
    try:
        contacts = get_all_contacts()
        response_obj = ContactManagementAPIResponse(contact_id="all", data={ "contacts": contacts }, message="All contacts retrieved successfully")
        return response_obj.response()
    except Exception as e:
        response_obj = ContactManagementAPIResponse(contact_id="Error", success=False, message=f"Error retrieving contacts, please try again.")
        return response_obj.response()

def retrieve_contact_by_id(contact_id: str) -> dict:
    try:
        contact = get_contact_by_id(contact_id=uuid.UUID(contact_id))
        if contact:
            response_obj = ContactManagementAPIResponse(contact_id=contact_id, data=contact.get_response_data(), message="Contact retrieved successfully")
        else:
            response_obj = ContactManagementAPIResponse(contact_id=contact_id, success=False, message="Contact not found")
        return response_obj.response()
    except Exception as e:
        response_obj = ContactManagementAPIResponse(contact_id=contact_id, success=False, message=f"Error retrieving contact, please try again.")
        return response_obj.response()

def create_contact(contact: dict) -> dict:
    try:
        contact_obj = convert_json_to_contact(contact)
        inserted_contact = insert_contact(contact=contact_obj)
        response_obj = ContactManagementAPIResponse(contact_id="123", data=inserted_contact.get_response_data(), message="Contact created successfully")

        return response_obj.response()
    except Exception as e:
        response_obj = ContactManagementAPIResponse(contact_id="Error", success=False, message=f"Error creating contact, please try again.")
        return response_obj.response()

def update_contact(contact_id: str, contact: dict) -> dict:
    try:
        contact_obj = convert_json_to_contact(contact)
        updated_contact = update_contact_by_id(contact_id=uuid.UUID(contact_id), contact=contact_obj)
        response_obj = ContactManagementAPIResponse(contact_id=contact_id, data=updated_contact.get_response_data(),
                                                    message="Contact updated successfully")
        return response_obj.response()
    except Exception as e:
        response_obj = ContactManagementAPIResponse(contact_id=contact_id, success=False, message=f"Error updating contact, please try again.")
        return response_obj.response()

def remove_contact(contact_id: str) -> dict:
    try:
        remove_contact_by_id(contact_id=uuid.UUID(contact_id))
        response_obj = ContactManagementAPIResponse(contact_id=contact_id, message="Contact removed successfully")
        return response_obj.response()
    except Exception as e:
        response_obj = ContactManagementAPIResponse(contact_id=contact_id, success=False, message=f"Error removing contact, please try again.")
        return response_obj.response()