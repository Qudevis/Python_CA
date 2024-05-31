
def suma(a,b):
    return a + b


def atimtis(a,b):
    return a - b



if __name__ == '__main__': # šitas suveiks tik tada, kai šis failas bus leidžiamas tiesiogiai, bet ne importuojamas
    # print("Sveiki as esu modulis")
    # print("Failo pabaiga")
    # svarbus_kintamasis = 15
    print(__name__) # '__main__'
else:
    # print("Aš nesu pagrindinis failas")
    print(__name__) # modulis_paskaita9