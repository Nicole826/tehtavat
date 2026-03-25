import random

def heita_noppa(tahkot):
    return random.randint (1, tahkot)

maksimi = int(input("Anna nopan maksimi silmäluku: "))

while True:
    tulos = heita_noppa(maksimi)
    print(tulos)
    if tulos == maksimi:
        break
