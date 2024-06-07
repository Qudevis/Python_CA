import sqlite3 as sl3


def InsertPerson(conn, name, last_name, age):
    cur = conn.cursor()
    cur.execute(f"Insert into people(Name, Last_Name, Age) Values(?,?, ?)",(name,last_name,age))
    conn.commit()

def InsertPersonNamed(conn, name, last_name, age):
    cur = conn.cursor()
    cur.execute(f"Insert into people(Name, Last_Name, Age) Values(:vardas,:pavarde, :amzius)",{"pavarde":last_name,"vardas":name,"amzius":age}) # :vardas = zodynas["vardas"]
    conn.commit()

path_to_db = "main_database.db"

conn = sl3.connect(path_to_db)

cur = conn.cursor()


cur.execute("""
Create table if not exists people
(
Id integer primary key autoincrement,
Name text not null,
Last_Name text not null,
Age integer

)
""")

conn.commit()

# name = input("Please enter your name: ")
# last_name = input("Please enter your last name: ")
# age = input("Please enter your age: ")

# InsertPersonNamed(conn,name,last_name,age)

class Person():
    def __init__(self,name,last_name,age) -> None:
        self.name = name
        self.last_name = last_name
        self.age = age
    def __repr__(self) -> str:
        return f"{self.name}|{self.last_name}"


people = cur.execute("Select * from people").fetchall()

people_objects = []

for person in people:
    zmogus = Person(person[1],person[2],person[3])
    people_objects.append(zmogus)


print(people_objects)

cur.execute("Delete From people Where Id = 14")
conn.commit()


conn.close()
