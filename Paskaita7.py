

# file = open("test.txt","a+")

# read_text = file.read()

# print(read_text)

# file.write("My name is Justas")



# file.close()



# with open("test.txt","r+") as file:

#     read_text = file.read()

#     print(read_text)

    #abc.write("My name is Justas")

# my_list = [5,7,8,89,4]

# i = 0

# for num in my_list:
#     print(f"skaicius {num} yra {i}-tas sarase")
#     i += 1

# for b, num in enumerate(my_list):
#     print(f"skaicius {num} yra {b}-tas sarase")

# with open("test.txt","r+") as file:

#     read_text = file.read()

#     file.write(read_text[::-1])



# from datetime import datetime

# zen = '''
# The Zen of Python, by Tim Peters

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!
# '''

# def atbulai(sakinys):
#     return sakinys[::-1]

# def patikrinti_sakini(sakinys):
#     print("Žodžių kiekis:", len(sakinys.split()))
#     print("Skaičių kiekis:", sum(c.isdigit() for c in sakinys))
#     print("Didžiųjų raidžių:", sum(c.isupper() for c in sakinys))
#     print("Mažųjų raidžių:", sum(c.islower() for c in sakinys))

# def didziosiomis(sakinys):
#     return sakinys.upper()

# # 1. Sukurti failą tekstas.txt su tekstu:

# with open('tekstas.txt', 'w') as failas:
#     failas.write(zen)

# # 2. Atspausdintų tekstą iš sukurto failą:

# with open('tekstas.txt', 'r') as failas:
#     print(failas.read())

# # 3. Paskutinėje sukurto failo eilutėje pridėtų šiandien datą:

# with open('tekstas.txt', 'a') as failas:
#     failas.write(str(datetime.today()))

# # 4. Sunumeruoti visas failo teksto eilutes (kiekvienos pradžioje pridėti skaičių):

# naujas = ""
# skaicius = 1
# with open('tekstas.txt', 'r') as failas:
#     for eilute in failas:
#         naujas += str(skaicius) + " " + eilute
#         skaicius += 1

# with open('tekstas.txt', 'w') as failas:
#     failas.write(naujas)


# # 5. Sukurtame faile eilutę "Beautiful is better than ugly." pakeisti į "Gražu yra geriau nei bjauru.":

# pakeitimas = ""

# with open('tekstas.txt', 'r') as failas:
#     pakeitimas = failas.read()

# pakeitimas = pakeitimas.replace("Beautiful is better than ugly.", "Gražu yra geriau nei bjauru.")

# with open('tekstas.txt', 'w', encoding="UTF-8") as failas:
#     failas.write(pakeitimas)

# # 6. Atspausdintų visą failo tekstą atbulai:

# with open('tekstas.txt', 'r') as failas:
#     print(atbulai(failas.read()))

# # 7. Atspausdintų, kiek failo tekste yra žodžių, skaičių, didžiųjų ir mažųjų raidžių:

# with open('tekstas.txt', 'r') as failas:
#     print(patikrinti_sakini(failas.read()))

# # 8. Nukopijuotų visą sukurto failą tekstą į naują failą, tik DIDŽIOSIOMIS RAIDĖMIS:

# with open('tekstas.txt', 'r', encoding="UTF-8") as nuskaitomas_failas:
#     with open('tekstas_didziosiomis.txt', "w", encoding="UTF-8") as irasomas_failas:
#         irasomas_failas.write(didziosiomis(nuskaitomas_failas.read()))

# from datetime import datetime

# pirmas = "Netuščias"
# tekstas = ""

# while pirmas != "":
#     pirmas = input("Įveskite eilutę: ")
#     if pirmas != "":
#         tekstas += pirmas + "\n"
#     else:
#         break

# failo_pavadinimas = input("Įveskite failo pavadinimą: ")

# with open(failo_pavadinimas + ".txt", "w", encoding="UTF-8") as failas:
#     failas.write(tekstas)


# import os
# from datetime import datetime

# # 1 Ant darbalaukio sukurtų naują katalogą "Mano Katalogas"

# try:
#     os.chdir('C:\\Users\\Donoras\\Desktop')
#     os.mkdir("Naujas katalogas")
# except:
#     "Toks katalogas jau yra"

# os.chdir('C:\\Users\\Donoras\\Desktop\\Naujas katalogas')

# # 2 Jame sukurtų failą "data.txt", kurios tektas - šiandienos data ir laikas

# with open("data.txt", "w") as failas:
#     failas.write(str(datetime.today()))

# # 3 Atspaudintų, kada naujas failas buvo modifikuotas ir kiek jis užima baitų
# os.chdir('C:\\Users\\Donoras\\Desktop\\Naujas katalogas')

# print("Sukūrimo data:", datetime.fromtimestamp(os.stat("data.txt").st_ctime)) #6155614544195.5741650165  
# print("Failo dydis:", os.stat("data.txt").st_size)


# import pickle

# while True:
#     try:
#         with open("biudzetas.pkl", "rb") as pickle_in:
#             biudzetas = pickle.load(pickle_in)
#             suma = 0
#             print("--------Įrašų sąrašas:---------")
#             for skaicius, irasas in enumerate(biudzetas):
#                 suma += irasas
#                 print(skaicius + 1, irasas)
#             print("Biudžeto balansas", suma)
#             print("-------------------------------")
#     except:
#         print("Nepavyko nuskaityti failo")
#         biudzetas = []
#     print("Norėdami išeiti palikite tuščią lauką ir spauskite ENTER")
#     irasas = input("Įveskite pajamas arba išlaidas: ")
#     if irasas == "":
#         break
#     irasas = float(irasas)
#     biudzetas.append(irasas)

#     try:
#         with open("biudzetas.pkl", "wb") as pickle_out:
#             pickle.dump(biudzetas, pickle_out)
#     except:
#         print("Nepavyko įrašyti failo")

# skaiciai = [4,8,9,5,6,-5]


# with open("naujas.pkl", "wb") as naujas:
#     pickle.dump(skaiciai,naujas)


# with open("naujas.pkl", "rb") as skaitomas:
#     tekstas = pickle.load(skaitomas)
#     with open("naujass.txt", "w") as tekstinis:
#         tekstinis.write(str(tekstas))


# failo_pavadinimas = input("Įveskite failo pavadinimą: ")

# with open(failo_pavadinimas, 'w+', encoding='utf-8') as failas:
    
#     print("Įveskite tekstą (tuščia eilutė baigia įvedimą):")
#     while True:
#         eilute = input()
#         if eilute == "":
#             break
#         failas.write(eilute + "\n")
#         failas.seek(0)
#         print(failas.read())
# print(f"Tekstas įrašytas į failą '{failo_pavadinimas}'")
# skaicius = 15.489589
# for i in range(0,50):
#     print('-'*30)
#     print(f"{i:>{10}.5f}|{i+1:<{10}.5f}")
#     print('-'*30)
# my_list = [5,7,9,8,9,4,2,4,5,1,1,1,2,2,2,3,3,3]
# tekstas = "Sveiki, mano vardas Sveiki, kaip jums Vardas sekasi, Justas, Man MAN Man Man Man Man"
# my_set = set(tekstas.split())

# print(my_set)

# for raid in tekstas: # raid = tekstas[0].... raid = tekstas[1].... raid = tekstas[2]......
#     print(raid)

# mano_tuple_sarasas = [(4,6,8),(1,7,9),(9,4,4),(5,15,8),(10,19,9)]

# for a,b,c in mano_tuple_sarasas: # a = mano_tuple_sarasas[0][0] b = mano_tuple_sarasas[0][1] ... a = mano_tuple_sarasas[1][0] b = mano_tuple_sarasas[1][1]...
#     print(f"{a}+{b}+{c}={sum((a,b,c))}")


skaiciai = [5,7,8,5,4,5,8]

# i = 0
# for skaicius in skaiciai:
#     print(f"skaicius {skaicius} yra {i} sarase")
#     i = i + 1


# for ind, skaicius in enumerate(skaiciai):
#     print(f"skaicius {skaicius} yra {ind} sarase")

# tekstas = "Labas kaip sekasi"

# tekstas.split() # ["labas", "kaip", "sekasi"]

# skaiciai2 = [4,9,5,1,2,3]
# skaiciai3 = [5,7,8,5,4,2,8]
# for skai in zip(skaiciai,skaiciai2):
#     print(skai)

vardai = ["Jonas","antanas","Mantas","Karolis"]

amziai = [15,54,21,23]

zodynas = dict(zip(vardai,amziai)) 

# print(zodynas)

# antano_amzius = zodynas["antanas"]

# a,b,c = ["Stalas","kede","lova"] 

# print(a)

# amziai.sort(reverse=True)
# print(amziai)
# print(zodynas.items())
# print(sorted(zodynas.items(),key=lambda x: x[1])) # zodynas items (Jonas, 15) x = (jonas, 15) x[1] - 15

# print(15 in amziai)



# if(16 in amziai):
#     print("egzistuoja sarase")
# else:
#     print("neegzistuoja")

# if("Jonas" in zodynas):
#     print(zodynas["Jonas"])


# mano_sarasas = [num for num in range(0,6)] # num = 0 mano_sarasas.append(0)... num = 1 mano_sarasas.append(1)

# for num in range(0,6):
#     mano_sarasas.append(num)

# print(mano_sarasas)

# skaiciai = [5,7,9]
# mano_sarasas = [num*2 for num in skaiciai] # num = 0 mano_sarasas.append(0)... num = 1 mano_sarasas.append(1)


# print(mano_sarasas)

skaiciai = [5,7,9,10]
# mano_sarasas = [num*2 for num in skaiciai if num % 2 ==0] # num = 0 mano_sarasas.append(0)... num = 1 mano_sarasas.append(1)

# for num in skaiciai:
#     if num % 2 ==0:
#         mano_sarasas.append(num*2)

# print(mano_sarasas)

# zodziai = ["labas",'Kaip',"sekasi"]
# print('----'.join(zodziai))



# # 15(20)
# print(20)

# skaicius = "bar"
# print(skaicius.islower())

# class MyClass():
#     def __init__(self) -> None:
#         pass
#     def suma(self):
#         raise NotImplementedError("Dar neigyvendinta")
    
#     def dalyba(self,a,b):
#         if(b == 0):
#             raise ZeroDivisionError("DALYBA IS NULIO")
#         else:
#             return a/b
# klase = MyClass()


# try:
#     print(klase.dalyba(7,0))
    
#     print("Suveikiau tinkamai")

# except Exception as e:
#     print(f"ivyko klaida {e}")

# skaiciai = [8,4,3]

# def cubed(x):
#     return x **3

# skaiciai_3 = map(cubed,skaiciai) # x = skaiciai[0].... return result = x ** 3 skaiciai_3 append(result) (Pakartojama len(skaiciai))
# skaiciai_3 = map(lambda x: x**3,skaiciai) # x = skaiciai[0].... return result = x ** 3 skaiciai_3 append(result) (Pakartojama len(skaiciai))

# print(list(skaiciai_3))

# def suma(a,b):
#     return a+b

# print(suma(4,9))


# lambda a,b: a+b # - suma

# mano_metodas = lambda a,b: a+b

# print(mano_metodas(5,9))

# tekstas = "4,8,9"


# iskirsytas = tekstas.split(',')

# print(iskirsytas)
# skaiciai_kon = []

# for x in iskirsytas:
#     tarpinis = int(x)*2
#     skaiciai_kon.append(tarpinis)




# # skaiciai_kon = map(lambda x: int(x)*2, tekstas.split(','))

# # print(list(skaiciai_kon))

# def sudaugink(x):
#      return int(x)*2
# lambda x: int(x)*2
# import calendar
# calendar.isleap

# import statistics
# skaiciai_test = [8,3,9,12,2]

# print(statistics.median(skaiciai_test))