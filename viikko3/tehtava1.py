# Kysytään kuhan pituus käyttäjältä
pituus = float(input("Anna kuhan pituus senttimetreinä: "))

# Alin sallittu pyyntimitta
alamitta= 37

#Tarkistetaan onko kuha alamittainen
if pituus < alamitta:
    puuttuu = alamitta - pituus
    print("Kuha on alamittainen.")
    print(f"Laske kuha takaisin järveen. Pyyntimitasta puuttuu {puuttuu: .1f} cm.")

else:
    print("Kuha on sallittua pyyntikokoa. Voit pitää sen.")
