naam_gebruiker = input("Geef je naam: ")
product = input("Welk product wil je kopen? ")
aantal = int(input("Hoeveel keer wil je " + product + " kopen? "))

prijs_per_stuk = 2
prijs_totaal = aantal * prijs_per_stuk

print("=============== BONNETJE ===============")
print("Klant: " + naam_gebruiker)
print(product)
print("Hoeveelheid: " + str(aantal))
print("Prijs per stuk: €" + str(prijs_per_stuk))
print("Subtotaal: €" + str(prijs_totaal))
print("Dank je voor je aankoop!")
print("========================================")