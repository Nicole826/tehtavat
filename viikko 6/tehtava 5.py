def parilliset(lista):
    return [luku for luku in lista if luku % 2 == 0]

luvut = [1, 2, 3, 4, 5, 6, 7]
uusi_lista = parilliset(luvut)

print("Alkuperäinen:", luvut)
print("Parilliset:", uusi_lista)
