# click.py
from sqlalchemy.orm import session
from sqlalchemy import Engine
import cli as click
from models import Base
from sqlalchemy.orm import Session
from sample import seed_data 
from commands import add_person, delete_person, list_persons
from models import Person  # Import other models as needed
from commands import add_criminal_record, delete_criminal_record, list_criminal_records
from commands import add_police_officer, delete_police_officer, list_police_officers
from commands import add_crime_scene, delete_crime_scene, list_crime_scenes
from commands import add_prison, delete_prison, list_prisons
from commands import add_prisoner, delete_prisoner, list_prisoners

@cli.group()
def cli():
    pass

@cli.command()
def init_db():
    """Initialize the database."""
    Base.metadata.create_all(bind=Engine)
    cli.echo("Database initialized.")

@cli.command()
def seed():
    """Seed initial data."""
    seed_data()

@cli.command()
@cli.option('--first_name', prompt='First Name', help='First name of the person.')
@cli.option('--last_name', prompt='Last Name', help='Last name of the person.')
@cli.option('--date_of_birth', prompt='Date of Birth', help='Date of birth (YYYY-MM-DD) of the person.')
def add_person_cmd(first_name, last_name, date_of_birth):
    """Add a person to the database."""
    data = {
        'first_name': first_name,
        'last_name': last_name,
        'date_of_birth': date_of_birth,
    }
    add_person(session, data)
    cli.echo("Person added successfully.")

@cli.command()
@cli.option('--person_id', prompt='Person ID', help='ID of the person to delete.')
def delete_person_cmd(person_id):
    """Delete a person from the database."""
    delete_person(session, person_id)
    cli.echo("Person deleted successfully.")

@cli.command()
def list_persons_cmd():
    """List all persons in the database."""
    list_persons(session)

# Similar commands for other tables (CriminalRecord, PoliceOfficer, CrimeScene, Prison, Prisoner)

cli.add_command(init_db)
cli.add_command(seed)
cli.add_command(add_person_cmd)
cli.add_command(delete_person_cmd)
cli.add_command(list_persons_cmd)

# Command for adding a criminal record
@cli.command()
@cli.option('--person_id', prompt='Person ID', help='ID of the person associated with the criminal record.')
@cli.option('--crime_type', prompt='Crime Type', help='Type of the crime.')
@cli.option('--crime_date', prompt='Crime Date', help='Date of the crime (YYYY-MM-DD).')
@cli.option('--description', prompt='Description', help='Description of the crime.')
@cli.option('--sentence', prompt='Sentence', help='Sentence for the crime.')
def add_criminal_record_cmd(person_id, crime_type, crime_date, description, sentence):
    """Add a criminal record to the database."""
    data = {
        'person_id': person_id,
        'crime_type': crime_type,
        'crime_date': crime_date,
        'description': description,
        'sentence': sentence,
    }
    add_criminal_record(session, data)
    cli.echo("Criminal record added successfully.")

# Command for deleting a criminal record
@cli.command()
@cli.option('--criminal_record_id', prompt='Criminal Record ID', help='ID of the criminal record to delete.')
def delete_criminal_record_cmd(criminal_record_id):
    """Delete a criminal record from the database."""
    delete_criminal_record(session, criminal_record_id)
    cli.echo("Criminal record deleted successfully.")

# Command for listing all criminal records
@cli.command()
def list_criminal_records_cmd():
    """List all criminal records in the database."""
    list_criminal_records(session)

# Add new commands to the CLI
cli.add_command(add_criminal_record_cmd)
cli.add_command(delete_criminal_record_cmd)
cli.add_command(list_criminal_records_cmd)

# Command for adding a police officer
@cli.command()
@cli.option('--first_name', prompt='First Name', help='First name of the police officer.')
@cli.option('--last_name', prompt='Last Name', help='Last name of the police officer.')
@cli.option('--badge_number', prompt='Badge Number', help='Badge number of the police officer.')
@cli.option('--rank', prompt='Rank', help='Rank of the police officer.')
@cli.option('--station', prompt='Station', help='Police station of the officer.')
def add_police_officer_cmd(first_name, last_name, badge_number, rank, station):
    """Add a police officer to the database."""
    data = {
        'first_name': first_name,
        'last_name': last_name,
        'badge_number': badge_number,
        'rank': rank,
        'station': station,
    }
    add_police_officer(session, data)
    cli.echo("Police officer added successfully.")

# Command for deleting a police officer
@cli.command()
@cli.option('--police_officer_id', prompt='Police Officer ID', help='ID of the police officer to delete.')
def delete_police_officer_cmd(police_officer_id):
    """Delete a police officer from the database."""
    delete_police_officer(session, police_officer_id)
    cli.echo("Police officer deleted successfully.")

# Command for listing all police officers
@cli.command()
def list_police_officers_cmd():
    """List all police officers in the database."""
    list_police_officers(session)

# Command for adding a crime scene
@cli.command()
@cli.option('--location', prompt='Location', help='Location of the crime scene.')
@cli.option('--date', prompt='Date', help='Date of the crime scene (YYYY-MM-DD).')
@cli.option('--description', prompt='Description', help='Description of the crime scene.')
@cli.option('--investigating_officer_id', prompt='Investigating Officer ID', help='ID of the investigating police officer.')
def add_crime_scene_cmd(location, date, description, investigating_officer_id):
    """Add a crime scene to the database."""
    data = {
        'location': location,
        'date': date,
        'description': description,
        'investigating_officer_id': investigating_officer_id,
    }
    add_crime_scene(session, data)
    cli.echo("Crime scene added successfully.")

# Command for deleting a crime scene
@cli.command()
@cli.option('--crime_scene_id', prompt='Crime Scene ID', help='ID of the crime scene to delete.')
def delete_crime_scene_cmd(crime_scene_id):
    """Delete a crime scene from the database."""
    delete_crime_scene(session, crime_scene_id)
    cli.echo("Crime scene deleted successfully.")

# Command for listing all crime scenes
@cli.command()
def list_crime_scenes_cmd():
    """List all crime scenes in the database."""
    list_crime_scenes(session)

# Command for adding a prison
@cli.command()
@cli.option('--name', prompt='Name', help='Name of the prison.')
@cli.option('--location', prompt='Location', help='Location of the prison.')
def add_prison_cmd(name, location):
    """Add a prison to the database."""
    data = {
        'name': name,
        'location': location,
    }
    add_prison(session, data)
    cli.echo("Prison added successfully.")

# Command for deleting a prison
@cli.command()
@cli.option('--prison_id', prompt='Prison ID', help='ID of the prison to delete.')
def delete_prison_cmd(prison_id):
    """Delete a prison from the database."""
    delete_prison(session, prison_id)
    cli.echo("Prison deleted successfully.")

# Command for listing all prisons
@cli.command()
def list_prisons_cmd():
    """List all prisons in the database."""
    list_prisons(session)

# Command for adding a prisoner
@cli.command()
@cli.option('--person_id', prompt='Person ID', help='ID of the person associated with the prisoner.')
@cli.option('--crime_id', prompt='Crime ID', help='ID of the criminal record associated with the prisoner.')
@cli.option('--entry_date', prompt='Entry Date', help='Entry date of the prisoner (YYYY-MM-DD).')
@cli.option('--release_date', prompt='Release Date', help='Release date of the prisoner (YYYY-MM-DD).')
@cli.option('--prison_id', prompt='Prison ID', help='ID of the prison where the prisoner is held.')
def add_prisoner_cmd(person_id, crime_id, entry_date, release_date, prison_id):
    """Add a prisoner to the database."""
    data = {
        'person_id': person_id,
        'crime_id': crime_id,
        'entry_date': entry_date,
        'release_date': release_date,
        'prison_id': prison_id,
    }
    add_prisoner(session, data)
    cli.echo("Prisoner added successfully.")

# Command for deleting a prisoner
@cli.command()
@cli.option('--prisoner_id', prompt='Prisoner ID', help='ID of the prisoner to delete.')
def delete_prisoner_cmd(prisoner_id):
    """Delete a prisoner from the database."""
    delete_prisoner(session, prisoner_id)
    cli.echo("Prisoner deleted successfully.")

# Command for listing all prisoners
@cli.command()
def list_prisoners_cmd():
    """List all prisoners in the database."""
    list_prisoners(session)

# Add new commands to the CLI
cli.add_command(add_police_officer_cmd)
cli.add_command(delete_police_officer_cmd)
cli.add_command(list_police_officers_cmd)

cli.add_command(add_crime_scene_cmd)
cli.add_command(delete_crime_scene_cmd)
cli.add_command(list_crime_scenes_cmd)

cli.add_command(add_prison_cmd)
cli.add_command(delete_prison_cmd)
cli.add_command(list_prisons_cmd)

cli.add_command(add_prisoner_cmd)
cli.add_command(delete_prisoner_cmd)
cli.add_command(list_prisoners_cmd)

if __name__ == '__main__':
    cli()
