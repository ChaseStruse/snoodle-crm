from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.company import Company

db_url = "sqlite:///company_management/companies.db"

def get_all_companies():
    SessionLocal = sessionmaker(bind=create_engine(db_url))
    with SessionLocal() as session:
        items = session.query(Company).all()
        return items