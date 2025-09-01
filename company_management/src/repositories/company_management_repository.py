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
    

def insert_company(company: Company) -> Company:
    SessionLocal = sessionmaker(bind=create_engine(db_url))
    print("Inserting company:", company.get_response_data())
    with SessionLocal() as session:
        session.add(company)
        session.commit()
        session.refresh(company)
        return company
    
