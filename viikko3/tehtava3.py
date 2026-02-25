sukupuoli = input("Anna biologinen sukupuoli (nainen/mies):")
hemoglobiini = float(input("Anna hemoglobiiniarvo (g/1):"))

if sukupuoli.lower() == "nainen":
    if hemoglobiini < 117:
        print("Hemoglobiiniarvo on alhainen.")
    elif hemoglobiini <= 175:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")

elif sukupuoli.lower() == "mies":
    if hemoglobiini < 134:
        print("Hemoglobiiniarvo on alhainen.")
    elif hemoglobiini <= 195:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")

else:
    print("Virheellinen sukupuoli.")