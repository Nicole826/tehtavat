while True:
    tuumat = float(input("Anna tuumamäärä (negatiivinen lopettaa): "))
    if tuumat < 0:
        print("Ohjelma lopetetaan.")
        break

    cm = tuumat * 2.54
    print(f"{tuumat} tuumaa on {cm: .2f} cm")
    