import random

salainen = random.randint(1,10)

while True:
    arvaus = int(input("Arvaa luku välilä 1-10:"))
    if arvaus > salainen:
        print("Liian suuri arvaus")
    elif arvaus < salainen:
        print("Liian pieni arvaus")
    else:
        print ("Oikein!")
        break