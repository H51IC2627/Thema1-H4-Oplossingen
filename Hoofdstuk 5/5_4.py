# Taartenwinkel: Programma waarin een klant taarten kan bestellen.

# Initialisatie variabelen
nog_bestellen = "ja"
taarten = []

# Taarten vragen zolang de klant nog wil bestellen.
while nog_bestellen == "ja":
    taart = input("Welke taart wil je bestellen? ")
    taarten.append(taart)

    nog_bestellen = input("Wil je nog een taart bestellen (ja/nee)?")

# Aan het einde de bestelling printen.
else:
    print("Je bestelling is: ")
    for taart in taarten:
        print(taart)