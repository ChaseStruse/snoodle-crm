from sqlalchemy import Column, String, Uuid, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Uuid, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    phone_number = Column(String, index=True)
    address = Column(String, index=True)
    date_of_birth = Column(Date, index=True)
    date_added = Column(Date, index=True)
    last_contacted = Column(Date, index=True)

    def get_response_data(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "email": self.email,
            "phone_number": self.phone_number,
            "address": self.address,
            "date_of_birth": self.date_of_birth.isoformat(),
            "date_added": self.date_added.isoformat(),
            "last_contacted": self.last_contacted.isoformat(),
        }
