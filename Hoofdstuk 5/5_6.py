# Priemgetal: Nakijken of een getal een priemgetal is.

getal = int(input("Voor welk getal wil je controleren of het een priemgetal is? "))
priemgetal = True

# 0 en 1 zijn geen priemgetallen.
if getal < 2:
    priemgetal = False
else:
    # Nakijken of het getal deelbaar is door een ander getal dan 1 en zichzelf.
    for i in range(2, getal):
        if getal%i == 0:
            priemgetal = False
            break

print(priemgetal)