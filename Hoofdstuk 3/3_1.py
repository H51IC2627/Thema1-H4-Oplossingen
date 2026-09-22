# Leeftijdscategorie: Bepaal de prijs van een bioscoopkaartje adhv de leeftijd.

leeftijd_gebruiker = int(input("Hoe oud ben jij? "))

# Prijs bepalen adhv leeftijd.
if leeftijd_gebruiker <= 5:
    prijs_ticket = 0
elif leeftijd_gebruiker <= 12:
    prijs_ticket = 4.5
elif leeftijd_gebruiker <= 18:
    prijs_ticket = 6
else:
    prijs_ticket = 8

print("Je moet " + str(prijs_ticket) + " euro betalen voor een biscoopkaartje.")