
# from statistics import mean, median

# # Atliktų veiksmus su skaičiais iki 50:

# skaiciai = list(range(51))

# # Padaugintų visus sąrašo skaičius iš 10 ir atspausdintų:

# # naujas = map(lambda x: x * 10, skaiciai) # 1 * 10 = ... 2 * 10 = .. 
# # print(list(naujas))  1 * 10 = 10... 2 * 10 = 20.. 

# # arba

# naujas = [x * 10 for x in skaiciai]
# print(naujas)

# # Atrinktų iš sąrašo skaičius, kurie dalinasi iš 7 ir atspausdintų

# # is_7 = filter(lambda x: x % 7 == 0, skaiciai) 
# # print(list(is_7))

# # arba

# is_7 = [x for x in skaiciai if x % 7 == 0]
# print(is_7)

# # Pakeltų visus sąrašo skaičius kvadratu ir atspausdintų

# # kvadratu = map(lambda x: x ** 2, skaiciai)
# # print(list(kvadratu))

# # arba

# kvadratu = [x ** 2 for x in skaiciai]
# print(kvadratu)

# # Su kvadratų sąrašu atliktų šiuos veiksmus: atspausdintų sumą,
# # mažiausią ir didžiausią skaičių, vidurkį, medianą

# print(sum(kvadratu))
# print(min(kvadratu))
# print(max(kvadratu))
# print(mean(kvadratu))
# print(median(kvadratu))

# # Surūšiuotų ir atspausdintų kvadratų sąrašą atbulai

# atbulai = sorted(kvadratu, reverse=True)
# print(atbulai)

# kvadratu.sort(reverse=True)
# print(kvadratu)


# # atbulai = kvadratu[::-1] 
# print(atbulai)


# print(type("5"))
# print(type("5") == int)


# sarasas = [4,7,9,"Tekstas",1.5]

# print(sum(list((type(c) is int) or (type(c) is float) for c in sarasas)))

# print(abs(-5))

# class Darbuotojas:
#     def __init__(self, name, last_name) -> None:
#         self.name = name
#         self.last_name = last_name

#     def __repr__(self) -> str:
#         return self.name
    
#     def __str__(self) -> str:
#         return self.name

# darb1 = Darbuotojas("Justas","Justaitis")
# darb2 = Darbuotojas("Antanas","Antanaitis")
# darb3 = Darbuotojas("Mantas","Mantanaitis")

# darbuotojai = [darb1,darb2,darb3]

# # surikiuoti = sorted(darbuotojai,key= lambda darbuotojas: darbuotojas.name)

# # # print(surikiuoti)

# # zodynas = {"Lukas":15,"Jonas":20,"Antanas":5}
# # print(zodynas)
# # surikiuotas_zod = sorted(zodynas.items(), key= lambda key_value_pair: key_value_pair[1] )

# # print(surikiuotas_zod)

# from operator import attrgetter

# surikiuotas_su_attr = sorted(darbuotojai,key=attrgetter("last_name"))

# print(surikiuotas_su_attr)






sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]

# Paskaičiuotų ir atspausdintų visų sąrašo skaičių sumą

# suma = sum(filter(lambda x: type(x) is int or type(x) is float, sarasas))
# print(suma)

# arba
stringai = sum(x for x in sarasas if type(x) is int or type(x) is float)
print(stringai)

# Sudėtų ir atspausdintų visus sąrašo žodžius
#
# sakinys = filter(lambda x: type(x) is str, sarasas)
# print(" ".join(sakinys))

# arba

sakinys = [x for x in sarasas if type(x) is str]
print(" ".join(sakinys))

# Suskaičiuotų ir atspausdintų, kiek sąrašę yra loginių (boolean)
# kintamųjų su True reikšme

# kiek = sum(filter(lambda x: type(x) is bool, sarasas))
# print(kiek)


# arba

kiek = sum([type(x) is bool for x in sarasas])
print(kiek)






from operator import attrgetter

# Turėtų klasę Zmogus, su savybėmis vardas ir amzius
# Klasėje būtų __repr__ metodas, kuris atvaizduotų vardą ir amžių

class Zmogus:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

    def __repr__(self):
        return (f"({self.vardas}, {self.amzius})")

# Inicijuoti kelis Zmogus objektus su vardais ir amžiais
# Įdėti sukurtus Zmogus objektus į naują sąrašą

z1 = Zmogus("Domas", 22)
z2 = Zmogus("Antanas", 30)
z3 = Zmogus("Jonas", 45)

sarasas = [z1, z2, z3]

# Surūšiuotų ir atspausdintų sąrašo objektus pagal vardą

surusiuotas = sorted(sarasas, key=lambda z: (z.vardas, z.amzius))
print(surusiuotas)

# arba

surusiuotas = sorted(sarasas, key=attrgetter("vardas"))
print(surusiuotas)

# Surūšiuotų ir atspausdintų sąrašo objektus pagal vardą atbulai

surusiuotas = sorted(sarasas, key=attrgetter("vardas"), reverse=True)
print(surusiuotas)

# Surūšiuotų ir atspausdintų sąrašo objektus pagal amžių

surusiuotas = sorted(sarasas, key=attrgetter("amzius","vardas"))
print(surusiuotas)

# Surūšiuotų ir atspausdintų sąrašo objektus pagal amžių atbulai

surusiuotas = sorted(sarasas, key=attrgetter("amzius"), reverse=True)
print(surusiuotas)
