sanat = ["omena", "tietokone", "kissa", "ohjelmointi", "auto", "kangas"]

maara = 0
for sana in sanat:
    if len(sana) > 5:
        maara += 1

print(f"Yli 5 kirjainta sisältäviä sanoja: {maara}")
