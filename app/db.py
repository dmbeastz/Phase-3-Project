# db.py
# To generate the database
from sqlalchemy import create_engine
from models import Base

engine = create_engine('sqlite:///criminal_database.db')
Base.metadata.create_all(engine)
