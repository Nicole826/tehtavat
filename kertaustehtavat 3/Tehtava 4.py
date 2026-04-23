import math

# 1. Luo funktio create_point(x, y)
def create_point(x, y):
    return (x, y)

# 2. Luo funktio distance(p1, p2)
def distance(p1, p2):
    # p1 = (x1, y1), p2 = (x2, y2)
    # Lasketaan etäisyys kaavalla: sqrt((x2-x1)^2 + (y2-y1)^2)
    d = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
    return d

# 3. Kysytään arvot käyttäjältä ja luodaan pisteet
print("Syötä ensimmäisen pisten koordinaatit:")
x1 = float(input("x1: "))
y1 = float(input("y1: "))
piste1 = create_point(x1, y1)

print("\nSyötä toisen pisteen koordinaatit:")
x2 = float(input("x2: "))
y2 = float(input("y2: "))
piste2 = create_point(x2, y2)

# 4. Kutsutaan funktiota ja lasketaan etäistts
etaisyys = distance(piste1, piste2)

# 5. Tulostetaan etäisyys pyöristettynä kahteen desimaaliin (lisätehtävä)
print(f"\nPisteiden {piste1} ja {piste2} välinen etäisyys 0n: {etaisyys: .2f}")




