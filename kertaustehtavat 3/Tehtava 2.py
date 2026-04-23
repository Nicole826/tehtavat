# Luodaan sanakirja: [nimi, vuosiluokka, lempiaine]
oppilaat = {
    "Ville": ["Ville", 5, "Matikka"],
    "Liisa": ["Liisa", 3, "Kuvataide"],
    "Eetu": ["Eetu", 9, "Historia"],
}
# Hae ja tulosta yhden vuosiluokka ja toisen lempiaine
print(f"Villen vuosiluokka: {oppilaat['Ville'][1]}")
print(f"Liisan lempiaine: {oppilaat['Liisa'][2]}")

# Muokkaa yhden oppilaan lempiaine
oppilaat ["Eetu"][2] = "Liikunta"

# Lisää uusi oppilas
oppilaat ["Sari"] = ["Sari", 7, "Biologia"]

# Poista yksi oppilas
del oppilaat ["Liisa"]

# Tulosta päivitetty sanakirja
print("\nPäivitetty oppilassanakirja (Tehtävä 2): ")
print(oppilaat)