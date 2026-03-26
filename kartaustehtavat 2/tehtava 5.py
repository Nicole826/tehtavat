def suurin_arvo(a, b,c):
    return max(a,b,c)

# Kysytään luvut käyttäjältä
luku1 = float(input("Anna ensimmäinen luku: "))
luku2 = float(input("Anna toinen luku: "))
luku3 = float(input("Anna kolmas luku: "))

# Tulostetaan suurin
print("Suurin arvo on:", suurin_arvo(luku1, luku2, luku3))
