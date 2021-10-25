from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Use connection string without password (adjust user/db/host/port as needed)
DATABASE_URL = "postgresql://ahil@localhost:5432/cat"

engine = create_engine(DATABASE_URL, echo=True)
