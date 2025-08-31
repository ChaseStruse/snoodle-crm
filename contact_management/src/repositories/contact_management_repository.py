from models.contact import Contact
from db import get_engine, get_all_items_from_db, insert_item_to_db
from sqlalchemy.orm import Session
from datetime import date
import uuid

DB_URL = "sqlite:///contact_management/contacts.db"

def insert_contact(contact) -> Contact:
    insert_item_to_db(contact, get_engine(DB_URL))
    return contact

def get_all_contacts() -> list[Contact]:
    contacts = get_all_items_from_db(object_to_query=Contact, engine=get_engine(DB_URL))
    return contacts

def get_contact_by_id(contact_id) -> Contact:
    with Session(get_engine()) as session:
        contact = session.query(Contact).filter(Contact.id == contact_id).first()
        session.close()
        return contact


def update_contact_by_id(contact_id: uuid.UUID, contact: Contact) -> Contact:
    with Session(get_engine(DB_URL)) as session:
        db_contact = session.query(Contact).filter(Contact.id == contact_id).first()
        if db_contact:
            db_contact.name = contact.name
            db_contact.email = contact.email
            db_contact.phone_number = contact.phone_number
            db_contact.address = contact.address
            db_contact.date_of_birth = contact.date_of_birth
            db_contact.last_contacted = contact.last_contacted
            session.commit()
            session.refresh(db_contact)
            session.close()

        session.close()
        return db_contact


def remove_contact_by_id(contact_id: uuid.UUID) -> bool:
    with Session(get_engine(DB_URL)) as session:
        db_contact = session.query(Contact).filter(Contact.id == contact_id).first()
        if db_contact:
            session.delete(db_contact)
            session.commit()
            session.close()
            return True
        session.close()
        return False