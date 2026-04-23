# 1 Luodaan sanakirja
henkilot = {
    "John" : ["John", 30, "Engineer"],
    "Emily" : ["Emily", 25, "Artist"],
    "Anna" : ["Anna", 22, "Student"]
}
# Hea ja tulosta: Johnin nimi ja ikä sekä Emilyn ammatti
# Indeksi 0 = nimi, 1 = ikä, 2 = ammatti
print(f"Johnin nimi: {henkilot ["John"][0]}, ikä: {henkilot["John"][1]}")
print(f"Emilyn ammatti: {henkilot["Emily"][2]}")

# Muokkaa: Anna -> Teacher ja lisää James
henkilot["Anna"][2] = "Teacher"
henkilot["James"] = ["James", 28, "Writer"]

# Lisää Sophia
henkilot ["Sophia"] = ["Sophia", 35, "Doctor"]

# Poista Emily
del henkilot ["Emily"]

# Tulosta lopullinen sanakirja
print("\nLopullinen sanakirja (Tehtava 1):")
print(henkilot)



