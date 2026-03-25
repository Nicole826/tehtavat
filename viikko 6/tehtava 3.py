def gallonat_litroiksi(gallonat):
    return gallonat * 3,785

while True:
    maara = float(input("Anna gallonamäärä: "))
    if maara < 0:
        break
    print("Litroina:", gallonat_litroiksi(maara))
    