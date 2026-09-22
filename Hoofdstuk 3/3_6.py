# Schoppen troef: De hoogste kaart wint, met schoppen als troefkleur.
import random
# Mogelijkheden kaarten.
kleuren = ["harten", "klaveren", "ruiten", "schoppen"]

# Namen spelers vragen.
gebruiker1 = input("Wat is de naam van speler 1? ")
gebruiker2 = input("Wat is de naam van speler 2? ")

# Willekeurige kaarten trekken.
kleur_gebruiker1 = random.choice(kleuren)
nummer_gebruiker1 = random.randint(2, 14)
kleur_gebruiker2 = random.choice(kleuren)
nummer_gebruiker2 = random.randint(2, 14)

# Nummer omzetten naar waardes.
if nummer_gebruiker1 == 11:
    waarde_gebruiker1 = "J"
elif nummer_gebruiker1 == 12:
    waarde_gebruiker1 = "Q"
elif nummer_gebruiker1 == 13:
    waarde_gebruiker1 = "K"
elif nummer_gebruiker1 == 14:
    waarde_gebruiker1 = "A"
else:
    waarde_gebruiker1 = str(nummer_gebruiker1)

if nummer_gebruiker2 == 11:
    waarde_gebruiker2 = "J"
elif nummer_gebruiker2 == 12:
    waarde_gebruiker2 = "Q"
elif nummer_gebruiker2 == 13:
    waarde_gebruiker2 = "K"
elif nummer_gebruiker2 == 14:
    waarde_gebruiker2 = "A"
else:
    waarde_gebruiker2 = str(nummer_gebruiker2)

print("Kaart " + gebruiker1 + ": " + kleur_gebruiker1 + " " + waarde_gebruiker1)
print("Kaart " + gebruiker2 + ": " + kleur_gebruiker2 + " " + waarde_gebruiker2)

# Winnaar bepalen
if kleur_gebruiker1 == "schoppen" and kleur_gebruiker2 != "schoppen":
    winnaar = gebruiker1
elif kleur_gebruiker2 == "schoppen" and kleur_gebruiker1 != "schoppen":
    winnaar = gebruiker2
else:
    if nummer_gebruiker1 > nummer_gebruiker2:
        winnaar = gebruiker1
    elif nummer_gebruiker1 < nummer_gebruiker2:
        winnaar = gebruiker2
    else:
        winnaar = "niemand"

print(winnaar + " wint.")