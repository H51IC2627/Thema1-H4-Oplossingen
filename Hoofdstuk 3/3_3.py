# Dobbelspel: Gooi een dobbelsteen voor 2 spelers en bepaal wie de hoogte worp had.
import random

# Namen gebruikers vragen.
gebruiker1 = input("Wat is de naam van speler 1? ")
gebruiker2 = input("Wat is de naam van speler 2? ")

# Dobbelsteen gooien voor elke gebruiker.
worp_gebruiker1 = random.randint(1,6)
worp_gebruiker2 = random.randint(1,6)

# Tonen wat elke speler gooide.
print(gebruiker1 + " gooit " + str(worp_gebruiker1) + ".")
print(gebruiker2 + " gooit " + str(worp_gebruiker2) + ".")

# Winnaar dobbelspel bepalen.
if worp_gebruiker1 > worp_gebruiker2:
    print(gebruiker1 + " wint.")
else:
    print(gebruiker2 + " wint.")