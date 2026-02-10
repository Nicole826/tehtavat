import random

#Kolminumeroinen koodi (0-9)
koodi1 = ""
for i in range(3) :
    koodi1 = koodi1 + str(random.randint(0,9))


#Nelinumeroinen koodi (1-6)
koodi2 = ""
for i in range(4) :
    koodi2 = koodi2 + str(random.randint(1,6))


print("Kolminumeroinen koodi:", koodi1)
print("Nelinumeroinen koodi:", koodi2)
