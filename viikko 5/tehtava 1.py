import random

n = int(input("Kuinka monta arpakuutiota heitetään: "))
summa = 0

for i in range(n):
    heitto = random.randint(1, 6)
    print(f"Heitto {i+1}: {heitto}")
    summa += heitto

print ("Silmälukujen summa:", summa)
