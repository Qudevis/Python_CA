import sqlalchemy as sqla

from sqlalchemy.orm import declarative_base, sessionmaker

engine = sqla.create_engine("sqlite:///main_database.db")

Base = declarative_base() # pagrindinis sqlalchemy elementas, kuriame yra surisimo (klases su lentele) logika

class Person(Base):
    __tablename__ = "People"
    id = sqla.Column(sqla.Integer,primary_key=True)
    name = sqla.Column("Name",sqla.String)
    last_name = sqla.Column("Last_Name",sqla.String)
    age = sqla.Column("Age",sqla.Integer)

    def __init__(self,name,last_name,age):
        self.name = name
        self.last_name = last_name
        self.age = age
    def __repr__(self):
        return f"{self.name}|{self.last_name}"

Base.metadata.create_all(engine) # sukuria nurodytas lenteles is klasiu


Session = sessionmaker(bind=engine) # priskiriame bėgikui kelia 

session = Session() # Sakome begikui pradeti darba

person = Person("Justas","Justaitis","29")

session.add(person)

session.commit()

people = session.query(Person).all() # paimk visus Person objektus is people lenteles

print(people)