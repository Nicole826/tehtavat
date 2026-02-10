from viikko2.tehtava2 import pinta_ala

kanta = float(input("Anna suorakulmion kanta:"))
korkeus = float(input("Anna suorakulmion korkeus:"))
piiri = 2 * (kanta + korkeus)
pinta_ala = kanta * korkeus
print("Suorakulmion pinta ala on", piiri)
print("Suorakulmion pinta ala on", pinta_ala)
