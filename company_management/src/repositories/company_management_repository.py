import uuid
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.company import Company, Base

db_url = "sqlite:///company_management/companies.db"

def create_tables(engine):
    Base.metadata.create_all(bind=engine)

def get_all_companies():
    SessionLocal = sessionmaker(bind=create_engine(db_url))
    with SessionLocal() as session:
        items = session.query(Company).all()
        return items
    

def get_company_by_id(company_id):
    SessionLocal = sessionmaker(bind=create_engine(db_url))
    with SessionLocal() as session:
        company = session.query(Company).filter(Company.id == company_id).first()
        return company
    

def insert_company(company: Company) -> Company:
    SessionLocal = sessionmaker(bind=create_engine(db_url))
    print("Inserting company:", company.get_response_data())
    with SessionLocal() as session:
        session.add(company)
        session.commit()
        session.refresh(company)
        return company
    
def update_company_by_id(company_id: uuid.UUID, company: Company) -> Company:
    SessionLocal = sessionmaker(bind=create_engine(db_url))
    with SessionLocal() as session:
        db_company = session.query(Company).filter(Company.id == company_id).first()
        if db_company:
            db_company.name = company.name
            db_company.business_contact_email = company.business_contact_email
            db_company.business_contact_phone_number = company.business_contact_phone_number
            db_company.address = company.address
            db_company.primary_contact_id = company.primary_contact_id
            session.commit()
            session.refresh(db_company)
            session.close()

        session.close()
        return db_company


def remove_company_by_id(company_id: uuid.UUID) -> bool:
    SessionLocal = sessionmaker(bind=create_engine(db_url))
    with SessionLocal() as session:
        db_company = session.query(Company).filter(Company.id == company_id).first()
        if db_company:
            session.delete(db_company)
            session.commit()
            session.close()
            return True
        session.close()
        return False
    
