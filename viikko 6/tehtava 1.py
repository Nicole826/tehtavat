import random

def heita_noppa():
    return random.randint(1, 6)


while True:
    tulos = heita_noppa()
    print(tulos)
    if tulos == 6:
        break