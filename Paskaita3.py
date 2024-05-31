

# skaicius = int(input("Iveskite skaiciu "))

# ar_skaicius_teigiamas = bool() # NEBUTINAS

# if skaicius > 0:
#     ar_skaicius_teigiamas = True #print("True")
# else:
#     ar_skaicius_teigiamas = False

# print(ar_skaicius_teigiamas)

import datetime as datetime

# siandien = datetime.datetime.today()
# print(siandien)


# print(datetime.date.today())

# print(datetime.datetime.today().time())

# data = datetime.datetime(2022,10,15, 10,15,10)

# print(data)

# print(data.strftime("%d %y")) #%H {}

# print(datetime.date.today().strftime("%j"))

# data = datetime.datetime(2022,10,15, 10,15,10)

# print(data - datetime.timedelta(days=30))

# print(data + datetime.timedelta(hours=30))
# print(data + datetime.timedelta(hours=30, days=3))

# ivesta_data = input("Iveskite gimimo data: ")
# gimimo_data = datetime.datetime.strptime(ivesta_data, "%Y-%m-%d")
# skirtumas = (datetime.datetime.now() - gimimo_data)
# print(skirtumas.days)
# print("jums yra: ",skirtumas.days / 365)
# # print("Jusu gimimo data yra: ", gimimo_data)

# from dateutil.relativedelta import relativedelta

# ivesta_data = input("Iveskite gimimo data: ")
# gimimo_data = datetime.datetime.strptime(ivesta_data, "%Y-%m-%d")
# skirtumas = relativedelta(datetime.datetime.today(), gimimo_data)
# print(skirtumas)

# ivesta_data = input("Iveskite gimimo data: ")
# gimimo_data = datetime.datetime.strptime(ivesta_data, "%Y-%m-%d")
# today = datetime.datetime.today()

# # Calculate the difference between today and the birthdate
# age = today.year - gimimo_data.year - ((today.month, today.day) < (gimimo_data.month, gimimo_data.day)) # True - 1 False - 0

# print(age)


# print(dt.datetime.today())


# import datetime
 
# #Prasome vartotojo ivesti data ir laika
# ivesta_data = input("iveskite gimimo data ir laika formatu 'YYYY-MM-DD HH:MM:SS': ")
 
# #Konvertuojama vartotojo ivestis
# gimimo_data = datetime.datetime.strptime(ivesta_data, "%Y-%m-%d %H:%M:%S")
 
# #Dabartinis laikas
# today = datetime.datetime.now()
 
# #Apskaiciuoti skirtuma nuo dabar ir nuo ivestos datos
# skirtumas = (datetime.datetime.now() - gimimo_data)
 
# # Apskaicuoti visus skirtumus
# metai = (skirtumas.days / 365)
# menesiai = (skirtumas.days / 30)
# dienos = (skirtumas.days)
# valandos = (skirtumas.total_seconds() / 3600) # 60- *60 = 3600
# minutes = (skirtumas.total_seconds() / 60)
# sekundes = (skirtumas.total_seconds())
 
# #Atspausdinti visus skirtumus
# print(f"nuo gimtadienio praejo: ")
# print(f"{round(metai)} metu")
# print(f"{round(menesiai)} menesiu")
# print(f"{dienos} dienu")
# print(f"{round(valandos)} valandu")
# print(f"{round(minutes)} minuciu")
# print(f"{round(sekundes)} sekundziu")

# "labas" - 5
# 7 / 0
# int("Hello")

try:
    # 7 / 0
    # int("Hello")
    # "labas" - 5
    try:
        open("Neegzistuojantis.txt")
    except:
        print("vidine klaida")
    
    print(7/1)
except ZeroDivisionError:
    print("Dalyba is nulio negalima")
    print()
except ValueError:
    print("Pateikta netinkama reiksme")
except TypeError:
    print("Neteisingas tipas")
except Exception as e: 
    print(e)
finally:
    print("Nesvarbu pavyko ar nepavyko as cia") #isjunk programa

print("Labas") #shift + alt + rodykle  zemyn - padublikuoti

# ctrl + f - surasti

# ctrl + h - pakeisti

print("Adsadsa") # ctrl + z - grizti atgal (atsaukti paskutini veiksma) undo

print("Fasdadsadsa") # ctrl + y atkurti kas buvo atsaukta redo


def printer(sarasas):
    for skaicius in sarasas:
        print(skaicius)

printer([5,7,9,8])

