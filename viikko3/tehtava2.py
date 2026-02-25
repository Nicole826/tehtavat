hyttiluokka = input("Anna laivan hyttiluokka (LUX, A, B, C):")
if hyttiluokka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hyttiluokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
else:
    print("Virheellinen hyttiluokka.")
