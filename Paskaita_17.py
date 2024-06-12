import sqlalchemy as sqla
from sqlalchemy.orm import declarative_base, sessionmaker

engine = sqla.create_engine("sqlite:///main_database.db")

Base = declarative_base() # pagrindinis sqlalchemy elementas, kuriame yra surisimo (klases su lentele) logika

class Person(Base):
    __tablename__ = "People" # cia skirta lenteles sukurimui
    id = sqla.Column(sqla.Integer,primary_key=True)
    name = sqla.Column("Name",sqla.String)
    last_name = sqla.Column("Last_Name",sqla.String)
    age = sqla.Column("Age",sqla.Integer)
    Gender = sqla.Column(sqla.String(1))

    def __init__(self,name,last_name,age): # cia jau kalba eina apie pati objekta Person
        self.name = name
        self.last_name = last_name
        self.age = age
    def __repr__(self):
        return f"{self.name}|{self.last_name}"
    
Base.metada.create_all(engine)
