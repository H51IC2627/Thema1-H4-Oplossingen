origineel_aantal_porties = 4
hoeveelheid_bloem = 200
hoeveelheid_eieren = 2

aantal_porties = int(input("Hoeveel porties wil je maken? "))

print("Origineel (" + str(origineel_aantal_porties) + " porties):")
print("- Bloem: " + str(hoeveelheid_bloem) + "g")
print("- Eieren: " + str(hoeveelheid_eieren))

hoeveelheid_bloem = hoeveelheid_bloem/origineel_aantal_porties*aantal_porties
hoeveelheid_eieren = hoeveelheid_eieren/origineel_aantal_porties*aantal_porties

print("Aangepast (" + str(aantal_porties) + " porties):")
print("- Bloem: " + str(hoeveelheid_bloem) + "g")
print("- Eieren: " + str(hoeveelheid_eieren))