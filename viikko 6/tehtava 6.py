import math

def pizzan_yksikkohinta(halkaisija_cm, hinta):
    sade_m = (halkaisija_cm / 100) / 2
    pinta_ala = math.pi * sade_m ** 2
    return hinta / pinta_ala

# Kysytään tiedot
h1 = float(input("Pizza 1 halkaisija (cm): "))
p1 = float(input("Pizza 1 hinta (€): "))

h2 = float(input("Pizza 2 halkaisija (cm): "))
p2 = float(input("Pizza 2 hinta (€): "))

y1 = pizzan_yksikkohinta(h1, p1)
y2 = pizzan_yksikkohinta(h2, p2)

print("Pizza 1 €/m^2:", y1)
print("Pizza 2 €/m^2:", y2)

if y1 < y2:
    print("Pizza 1 on parempi vastine rahalle")
elif y2 < y1:
    print("Pizza 2 on parempi vastine rahalle")
else:
    print("Molemmat ovat yhtä hyviä")