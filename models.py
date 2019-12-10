import uuid
from sqlalchemy import Column, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from database import Base, db_session


class Pet(Base):
    __tablename__ = 'pets'

    id = Column(String(50), primary_key=True)
    name = Column(String(50))
    type = Column(String(50))
    available = Column(Boolean())
    addedAt = Column(String(50))
    adoptedAt = Column(String(50))
    description = Column(String(50))
    shelterId = Column(String(50), ForeignKey('shelters.id'))

    def __init__(self, name, type, available, addedAt, adoptedAt, description, shelterId, id=None):
        self.name = name
        self.type = type
        self.available = available
        self.addedAt = addedAt
        self.adoptedAt = adoptedAt
        self.description = description
        self.shelterId = shelterId
        self.id = id or uuid.uuid4().hex

    def json(self):
        return {
            'name': self.name,
            'type': self.type,
            'available': self.available,
            'addedAt': self.addedAt,
            'adoptedAt': self.adoptedAt,
            'description': self.description,
            'shelterId': self.shelterId,
            'id': self.id
        }

    def save_to_db(self):
        db_session.add(self)
        db_session.commit()

    def delete_from_db(self):
        db_session.delete(self)
        db_session.commit()


class Shelter(Base):
    __tablename__ = 'shelters'

    id = Column(String(50), primary_key=True)
    name = Column(String(50))
    fullAddress = Column(String(50))
    city = Column(String(50))
    pets = relationship("Pet", backref="shelters", lazy='dynamic')

    def __init__(self, name, fullAddress, city, id=None):
        self.name = name
        self.fullAddress = fullAddress
        self.city = city
        self.id = id or uuid.uuid4().hex

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "fullAddress": self.fullAddress,
            "city": self.city,
            "petsAvailable": len(self.pets.all())
        }

    def save_to_db(self):
        db_session.add(self)
        db_session.commit()
