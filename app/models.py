# models.py
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base()

class Person(Base):
    __tablename__ = 'persons'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(Date)
    gender = Column(String)
    nationality = Column(String)
    address = Column(String)
    phone_number = Column(String)
    email = Column(String)

    criminal_records = relationship("CriminalRecord", back_populates="person")
    prisoners = relationship("Prisoner", back_populates="person")

class CriminalRecord(Base):
    __tablename__ = 'criminal_records'

    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('persons.id'))
    crime_type = Column(String)
    crime_date = Column(Date)
    description = Column(String)
    sentence = Column(String)

    person = relationship("Person", back_populates="criminal_records")

class PoliceOfficer(Base):
    __tablename__ = 'police_officers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    badge_number = Column(String)
    rank = Column(String)
    station = Column(String)

    crime_scenes = relationship("CrimeScene", back_populates="investigating_officer")

class CrimeScene(Base):
    __tablename__ = 'crime_scenes'

    id = Column(Integer, primary_key=True)
    location = Column(String)
    date = Column(Date)
    description = Column(String)
    investigating_officer_id = Column(Integer, ForeignKey('police_officers.id'))

    investigating_officer = relationship("PoliceOfficer", back_populates="crime_scenes")

class Prison(Base):
    __tablename__ = 'prisons'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)

    prisoners = relationship("Prisoner", back_populates="prison")

class Prisoner(Base):
    __tablename__ = 'prisoners'

    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('persons.id'))
    crime_id = Column(Integer, ForeignKey('criminal_records.id'))
    entry_date = Column(Date)
    release_date = Column(Date)
    prison_id = Column(Integer, ForeignKey('prisons.id'))

    person = relationship("Person", back_populates="prisoners")
    prison = relationship("Prison", back_populates="prisoners")
