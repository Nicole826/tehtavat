tuntipalkka = float(input("Tuntipalkka: "))
tunnit = float(input("Tehdyt tunnit:"))
paiva = input("Viikonpäivä: ")

if paiva.lower() == "sunnuntai" :
    paivapalkka = tuntipalkka * 2 * tunnit
else:
    paivapalkka = tuntipalkka * tunnit

print("Paivapalkka:" , paivapalkka, "euroa")

