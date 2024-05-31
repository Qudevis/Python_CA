#import this
import random
# print("hello")

# organization_Name = "Microsoft"
# est_year = 1985


# print('-'*45)
# print(f'|\tOrg_Name\t|\test_Year    |')
# print('-'*45)
# print(f'|\t{organization_Name}\t|\t{est_year}\t    |')
# print('-'*45)
# print(f'|\t{organization_Name}\t|\t{est_year}\t    |')
# print('-'*45)
# print(f'|\t{organization_Name}\t|\t{est_year}\t    |')

# print('-'*45)

# skaicius1 = int(input("Iveskite pirma skaiciu "))
# skaicius2 = int(input("Iveskite antra skaiciu "))

# rezultatas = skaicius1 == skaicius2
# print(rezultatas)


# rezultatas = (float(-0.28) - float(4.59-4.87)) < 0.00000000000001
# print(rezultatas)

# amzius = 20

# if amzius > 20:
#     print("Tu vyresnis nei 20")
#     if amzius > 80:
#         print("Tu esi ne tik vyresnis nei 20, tu esi senas")
#         if amzius >= 100:
#             print("tu ne tik senas bet ir rekoridininkas")
#         print('Taip pamirsau pamineti tu esi senjoras')
#     print("Tu galimai nesi toks senas")
# if amzius > 18 and amzius <= 20:
#     print('Tu gali pirkti gerimus')
# elif amzius > 20 and amzius < 45:
#     print('Tu gali nusipirkti alkoholio')
# elif amzius > 45:
#     print("Tu gali buti prezidentas")
# else:
#     print("Tu dar per jaunas")

# match amzius:
#     case 50: # if amzius == 50 # if amzius > 50
#         print("Tau yra virs 50 ")
#     case 20: # elif amzius == 20 
#         print("Tau yra 20")
#         print("Taip pat tu dar jaunas")
#         print("Tau tik prasid4jo gyvenimas")
#         if 8 > 7:
#             print("Taip pat vidine salyga yra teisinga")
#             if 1 > 5:
#                 print("Going deep")
#         elif 7 > 9:
#             print("Something")
#         else:
#             print("Else")
#     case _: # else
#         print("Neatitinka nei vienas variantas")




# zodis = "Zen of Python"

# atskirti_zodziai = zodis.split()

# print(atskirti_zodziai[1][-1])

# if 5> 7:
#     print("Hello")
# elif 8 > 9:
#     print("again")
# else:
#     print("Something wrong")



# zodziai = "Labas kaip tau sekasi, man tai gerai 5".split()

# print(zodziai)

# skaiciai = [5,7,9]


# print(zodziai[-1])

# boolai = [True,False,True,True,False]
# print(boolai[:4])

# skaiciu_skaiciai = [skaiciai,[8,4,9],skaiciai,skaiciai]
# print(skaiciu_skaiciai)

# skaiciai.append(15)
# skaiciai.append(19)
# skaiciai.extend(skaiciai)

# print(skaiciai)

# skaiciai[0] = 8
# print(skaiciai)
# # skaiciai.pop(0)
# # print(skaiciai)

# print(len(skaiciai))

# zodis = "televizorius"
# print(len(zodis))

# skaiciai = [5,7,9,5]
# print(skaiciai[-1])

# pazymiai = {"Justas": [7,5,9], "Paulius":[1,4,9], "Karolis": [9,5,9]}
# print(pazymiai)

# print(pazymiai['Paulius'])
# skaiciai = [[7,5,9], [1,4,9],[7,5,9]]

# skaiciai = [5,7,9,5]
# # skaiciai = {0:5,1:7,2:9,3:5}

# kompanijos = {"CodeAcademy":["Justas","Paulius","Edvinas"], 
#               "Maxima":["Arturas","Jonas"]}

# # print(kompanijos["Maxima"])

# kompanijos["Norfa"] = ["Laura","Tomas"]

# # del kompanijos["Maxima"]
# # print(kompanijos)
# kompanijos["Norfa"].append("Karolis")
# print(kompanijos)

# suma = 0

# for skaicius in skaiciai:
#     suma += skaicius
#     print("Dabartine suma: ", suma)
# print("Galutinis vidurkis",suma/len(skaiciai))

# for raktas, reiksme in kompanijos.items():
#     print(f"{raktas} darbuotojai yra: {reiksme}")

# for skaicius in range(50):
#     print(skaicius)

# limitas = 100
# i = 1
# while i < limitas:
#     print(i)
#     i +=1

# Input 15.... 

# for skaicius in range(10):
#     print("Pirmas spausdinimas", skaicius)
#     if(skaicius >= 3):
#         continue 
#     print(skaicius)


# for skaicius in range(10):
#     print(skaicius)
# else:
#     print("Pabaiga")



# amzius = int("20")
# amzius = int(input("Iveskite savo amziu "))



# if (amzius < 21):
#     print("POLICIJA")
# elif amzius > 18:
#     print("Gali nusipirkti energetini") 
# else:
#     print("Ifas nesuveike")
#     print("Labai nesuveike")

# if(amzius > 20):
#     print("Gali nusipirkti alkoholio")

# if(amzius > 65):
#     print("Tu esi senjoras")


# pinigai = 20

# if pinigai >= 500 and pinigai < 1500:
#     print("Dar pinigu pakanka")
# elif pinigai > 1500 and pinigai < 5000:
#     print("Turi daug pinigu")
# elif pinigai > 5000:
#     print("Tu esi turtingas")
# else:
#     print("Tu esi vargsas")

# skaicius = 5
# skaicius1 = 8
# skaicius2 = 15

# skaiciai = [skaicius,skaicius1,skaicius2,20]

# print(skaiciai)

# print(skaiciai[2])
# skaiciai.append(101)

# skaiciai.pop(3)

# skaiciai[0] = 1
# print(skaiciai)

# amziai = {"Arnas":[5,7,9],"Vaidas":15,"Karolina":25}

# print(amziai['Arnas'])

# greiciai = {1:7,2:7.15,3:8}

# print(greiciai[1])

# greiciai[4] = 8.20

# greiciai[1] = 6.58

# del greiciai[4]

# print(greiciai)

# suma = 0
# kiekis = int(input("Iveskite kieki "))
# for skaicius in range(kiekis): # if skaicius < 10: suma = suma + skaicius
#     print(skaicius)
#     if (skaicius % 2) == 0:
#         suma += skaicius # suma = suma + skaicius
# print(suma)

# suma = 0
# skaiciai = [5,7,9,1,5,4]

# for skaicius in skaiciai: # if skaicius < 10: suma = suma + skaicius
#     # print(skaicius)
#     if (skaicius % 2) == 0:
#         suma += skaicius # suma = suma + skaicius
# print(suma)

# amziai = {"Arnas":10,"Vaidas":15,"Karolina":25}

# for vardas, amzius in amziai.items():
#     print(amzius)
# kiekis = 0
# while 10>3:
#     print("Labas")
#     if input("Ivesk kazka ") == '':
#         break
# kiekis_vid = 0
# while kiekis < 10:
#     print("Isorinio ciklo kiekis: ", kiekis)
#     while kiekis_vid < 5:
#         print(f"Vidinio ciklo kiekis: {kiekis_vid}")
#         kiekis_vid += 1
#         if kiekis_vid == 3:
#             break
#     kiekis = kiekis + 1
#     kiekis_vid = 0


# skaiciai = [5,7,9,1,5,4]
# kiekis = 0
# while kiekis < len(skaiciai):
#     print(skaiciai[kiekis])
#     kiekis = kiekis + 1

# my_list = [1, 2, 3]
# print(4 in my_list)


# my_tuple = (1, 2, 3)
# print(my_tuple[0])

# kiekis = 0
# suma = 0
# while kiekis < 100000000:
#     suma += kiekis
#     kiekis += 1
# print(suma)

# a = 200
# b = 450
# print("A") if a > b else print("B")

# if 5 > 1:
#     pass
# print("hi")

# my_list = []
# if not my_list:
#   print("oh no, list is empty")

# d = {'a': 10, 'b': 20, 'c': 30}
# result = d.pop('a')
# print(result)
# print(d)

# dict_one = {'a': 10, 'b': 20, 'c': 30}
# dict_two = {'b': 200, 'd': 400}
# dict_one .update(dict_two )
# print(dict_one )

# test_keys = ["Albert", "Tom", "Stephen"]
# test_values = [1, 4, 5]
# my_dictionary= dict(zip(test_keys, test_values))
# print(my_dictionary)