# to connect to the database to postgresql

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base

# username= postgres , password=root

DATABASE_URL = "postgresql://postgres:swapnil@localhost:5432/ecomm"

# search for url & connect to database

engine = create_engine(DATABASE_URL)

# create session 

'''
bind : -- > to bind engine and seesion 
autocommit -- > Not to commit automaticaly '''

SessionLocal= sessionmaker(autocommit=False,autoflush=False,bind=engine)

# to carry data
Base = declarative_base()