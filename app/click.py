# click.py
from sqlalchemy.orm import session
from sqlalchemy import Engine
from models import Base
from sqlalchemy.orm import Session
from sample import seed_data, click
from commands import add_person, delete_person, list_persons
from models import Person  # Import other models as needed
from commands import add_criminal_record, delete_criminal_record, list_criminal_records
from commands import add_police_officer, delete_police_officer, list_police_officers
from commands import add_crime_scene, delete_crime_scene, list_crime_scenes
from commands import add_prison, delete_prison, list_prisons
from commands import add_prisoner, delete_prisoner, list_prisoners

@click.group()
def cli():
    pass

@click.command()
def init_db():
    """Initialize the database."""
    Base.metadata.create_all(bind=Engine)
    click.echo("Database initialized.")

@click.command()
def seed():
    """Seed initial data."""
    seed_data()

@click.command()
@click.option('--first_name', prompt='First Name', help='First name of the person.')
@click.option('--last_name', prompt='Last Name', help='Last name of the person.')
@click.option('--date_of_birth', prompt='Date of Birth', help='Date of birth (YYYY-MM-DD) of the person.')
def add_person_cmd(first_name, last_name, date_of_birth):
    """Add a person to the database."""
    data = {
        'first_name': first_name,
        'last_name': last_name,
        'date_of_birth': date_of_birth,
    }
    add_person(session, data)
    click.echo("Person added successfully.")

@click.command()
@click.option('--person_id', prompt='Person ID', help='ID of the person to delete.')
def delete_person_cmd(person_id):
    """Delete a person from the database."""
    delete_person(session, person_id)
    click.echo("Person deleted successfully.")

@click.command()
def list_persons_cmd():
    """List all persons in the database."""
    list_persons(session)

# Similar commands for other tables (CriminalRecord, PoliceOfficer, CrimeScene, Prison, Prisoner)

cli.add_command(init_db)
cli.add_command(seed)
cli.add_command(add_person_cmd)
cli.add_command(delete_person_cmd)
cli.add_command(list_persons_cmd)

if __name__ == '__main__':
    cli()
