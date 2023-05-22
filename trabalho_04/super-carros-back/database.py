from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+mysqldb://root:12345678@localhost:3306/superr-carros")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  
Base = declarative_base()

def get_db():     
    db = SessionLocal()     
    try:         
        yield db     
    finally:
        db.close()