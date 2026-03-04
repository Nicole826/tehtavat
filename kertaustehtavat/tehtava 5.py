while True:
    print("\nValitse toiminto:")
    print("1 = Yhteenlasku")
    print("2 = Vähennyslasku")
    print("3 = Kertolasku")
    print("4 = Jakolasku")
    print("5 = Lopeta")

    valinta = input("Valintasi: ")
    if valinta == "0":
        break

    luku1 = float(input("Anna ensimmäinen luku: "))
    luku2 = float(input("Anna toinen luku: "))

    if valinta == "1":
        print("Tulos:", luku1 + luku2)
    elif valinta == "2":
        print("Tulos:", luku1 - luku2)
    elif valinta == "3":
        print("Tulos:", luku1 * luku2)
    elif valinta == "4":
        if luku2 != 0:
            print("Tulos:", luku2 / luku1)
        else:
            print("Nollalla ei voi jakaa. ")
    else:
        print("Virheellinen valinta")
print ("Ohjelma lopetettu.")
