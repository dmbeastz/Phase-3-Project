# commands.py
from sqlalchemy.orm import Session
from models import Person, CriminalRecord, PoliceOfficer, CrimeScene, Prison, Prisoner

def add_person(session: Session, data):
    person = Person(**data)
    session.add(person)
    session.commit()

def delete_person(session: Session, person_id):
    person = session.query(Person).get(person_id)
    if person:
        session.delete(person)
        session.commit()

def list_persons(session: Session):
    persons = session.query(Person).all()
    for person in persons:
        print(f"ID: {person.id}, Name: {person.first_name} {person.last_name}, DOB: {person.date_of_birth}")

# CriminalRecord

def add_criminal_record(session: Session, data):
    criminal_record = CriminalRecord(**data)
    session.add(criminal_record)
    session.commit()

def delete_criminal_record(session: Session, record_id):
    criminal_record = session.query(CriminalRecord).get(record_id)
    if criminal_record:
        session.delete(criminal_record)
        session.commit()

def list_criminal_records(session: Session):
    criminal_records = session.query(CriminalRecord).all()
    for record in criminal_records:
        print(f"ID: {record.id}, Person: {record.person.full_name()}, Crime Type: {record.crime_type}")

# PoliceOffice 

def add_police_officer(session: Session, data):
    police_officer = PoliceOfficer(**data)
    session.add(police_officer)
    session.commit()

def delete_police_officer(session: Session, officer_id):
    police_officer = session.query(PoliceOfficer).get(officer_id)
    if police_officer:
        session.delete(police_officer)
        session.commit()

def list_police_officers(session: Session):
    police_officers = session.query(PoliceOfficer).all()
    for officer in police_officers:
        print(f"ID: {officer.id}, Name: {officer.first_name} {officer.last_name}, Badge: {officer.badge_number}")

# CrimeScene

def add_crime_scene(session: Session, data):
    crime_scene = CrimeScene(**data)
    session.add(crime_scene)
    session.commit()

def delete_crime_scene(session: Session, scene_id):
    crime_scene = session.query(CrimeScene).get(scene_id)
    if crime_scene:
        session.delete(crime_scene)
        session.commit()

def list_crime_scenes(session: Session):
    crime_scenes = session.query(CrimeScene).all()
    for scene in crime_scenes:
        print(f"ID: {scene.id}, Location: {scene.location}, Date: {scene.date}, Investigating Officer: {scene.investigating_officer.full_name()}")

# Prison

def add_prison(session: Session, data):
    prison = Prison(**data)
    session.add(prison)
    session.commit()

def delete_prison(session: Session, prison_id):
    prison = session.query(Prison).get(prison_id)
    if prison:
        session.delete(prison)
        session.commit()

def list_prisons(session: Session):
    prisons = session.query(Prison).all()
    for p in prisons:
        print(f"ID: {p.id}, Name: {p.name}, Location: {p.location}")

# Prisoner

def add_prisoner(session: Session, data):
    prisoner = Prisoner(**data)
    session.add(prisoner)
    session.commit()

def delete_prisoner(session: Session, prisoner_id):
    prisoner = session.query(Prisoner).get(prisoner_id)
    if prisoner:
        session.delete(prisoner)
        session.commit()

def list_prisoners(session: Session):
    prisoners = session.query(Prisoner).all()
    for p in prisoners:
        print(f"ID: {p.id}, Person: {p.person.full_name()}, Prison: {p.prison.name}, Entry Date: {p.entry_date}, Release Date: {p.release_date}")