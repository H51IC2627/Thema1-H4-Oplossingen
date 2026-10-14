# Duplicaten: Zoek de duplicaten in een lijst.

namen = ["Jan", "Piet", "Jan", "Joris", "Corneel"]
duplicaten = []

# Voor elke naam controleren hoe vaak hij voorkomt.
for naam in namen:
    aantal = namen.count(naam)

    # Nakijken of een naam meer dan 1 keer voorkomt en of hij al eerder is geteld.
    if aantal > 1 and naam not in duplicaten:
        print(naam + " komt " + str(aantal) + " keer voor.")
        duplicaten.append(naam)
