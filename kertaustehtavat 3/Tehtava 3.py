# Luodaan sanakirja ’Kirjasto’: [kirjoittaja, julkaisuvuosi, genre]
kirjasto = {
    "Tungematon sotilas": ["Väinö Linna", 1954, "Sotaviihde"],
    "Sinuhe eggyptiläinen": ["Mika Waltari", 1945, "Historiallinen"],
    "Harry Potter" : ["J.K Rowling", 1997, "Fantasia"]
}

# Hea ja tulosta yhden kirjoittaja ja toisen genre
print(f"Sinuhen kirjoittaja: {kirjasto["Sinuhe egyptiläinen"][0]}")
print(f"Harry Potterin genre: {kirjasto["Harry Potter"][2]}")

# Muokkaa yhden kirjan genre
kirjasto["Tuntematon sotilas"][2] = "Klassikko"

# Lisää uusi kirja
kirjasto ["Seitsemän veljestä"] = ["Aleksis Kivi", 1870, "Klassikko"]

# Poista yksi olemassa oleva kirja
del kirjasto["Harry Potter"]

# Tulosta päivitetty sanakirja
print("\nPäivitetty kirjasto (Tehtävä 3):")
print(kirjasto)