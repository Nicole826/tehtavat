luvut = []

while True:
    syote = input( "Anna luku (Enter lopettaa):")
    if syote == "":
        break

    luku = float(syote)
    luvut .append( luku )

if len(luvut) > 0 :
    print("Pienin:", min(luvut))
    print("Suurin:", max(luvut))
else:
    print("Lukuja ei annettu.")
