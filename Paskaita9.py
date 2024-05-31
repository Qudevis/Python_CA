


# import modulis_paskaita9 as mp

# print(mp.suma(5,9))


# print(mp.svarbus_kintamasis)


# from modulis_paskaita9 import svarbus_kintamasis as kintamasis


# print(kintamasis)

# from modulis_paskaita9 import atimtis as atm
# from modulis_paskaita9 import suma as sm
# from modulis_paskaita9 import suma,atimtis


# print(atm(4,9))

# from modulis_paskaita9 import suma as sm, svarbus_kintamasis as kint

# print(sm(7,9))

# from modulis_paskaita9 import * 
# atimtis()


# import modulis_paskaita9


# print("Paskaita9.py dabartinis vardas: " +__name__)


# import Moduliai.Paskaita9_Modulis2 as mp2


# mp2.daugyba(4,9)

# import pandas as pd






# if __name__ == '__main__': # šitas suveiks tik tada, kai šis failas bus leidžiamas tiesiogiai, bet ne importuojamas
#     print("Aš esu pagrindinis failas, ir mano nepakeistas pavadinimas yra Paskaita9")


class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    
    def __repr__(self):
        return f"Person(name={self.name}, age={self.age}, email={self.email})"

# Create instances
person1 = Person("Alice", 30, "alice@example.com")
person2 = Person("Bob", 25, "bob@example.com")
person3 = Person("Charlie", 35, "charlie@example.com")

# Store instances in a dictionary
people = {
    "alice": person1,
    "bob": person2,
    "charlie": person3
}

# Access a specific person
print(people["alice"])

# Add a new person
person4 = Person("David", 40, "david@example.com")
people["david"] = person4

# Iterate over the dictionary
for key, person in people.items():
    print(f"Key: {key}, Value: {person}")

# Update an attribute of a specific person
people["bob"].email = "newbob@example.com"
print(people["bob"])
