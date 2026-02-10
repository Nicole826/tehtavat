leiviskat = int(input("Anna leiviskät:"))
naulat = int(input("Anna naulat:"))
luodit = int(input("Anna luodit:"))

# Muutokset
luodit_yhteensä = leiviskat *20*32 + naulat *32 + luodit
grammat = luodit_yhteensä *13.3
kilot = int(grammat // 1000)
grammat = grammat % 1000
print("Massa on", kilot, "kg ja", grammat, "g")

