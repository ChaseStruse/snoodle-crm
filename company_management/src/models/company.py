from sqlalchemy import Column, String, Uuid, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Company(Base):
    __tablename__ = "companies"
    id = Column(Uuid, primary_key=True, index=True)
    name = Column(String, index=True)
    business_contact_email = Column(String, index=True)
    business_contact_phone_number = Column(String, index=True)
    address = Column(String, index=True)
    date_added = Column(Date, index=True)
    primary_contact_id = Column(Uuid, index=True)

    def get_response_data(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "business_contact_email": self.business_contact_email,
            "business_contact_phone_number": self.business_contact_phone_number,
            "address": self.address,
            "date_added": self.date_added.isoformat(),
            "primary_contact_id": str(self.primary_contact_id) if self.primary_contact_id is not None else "",
        }
