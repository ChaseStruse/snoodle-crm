from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.contact import Base

def create_tables(engine):
    Base.metadata.create_all(bind=engine)

def get_engine(db_url=""):
    engine = create_engine(db_url)
    return engine

def get_all_items_from_db(object_to_query, engine):
    SessionLocal = sessionmaker(bind=engine)
    with SessionLocal() as session:
        items = session.query(object_to_query).all()
        return items
    
def insert_item_to_db(item, engine):
    SessionLocal = sessionmaker(bind=engine)
    with SessionLocal() as session:
        session.add(item)
        session.commit()
        session.refresh(item)
        return item
    