# Fibonacci: Reeks van Fibonacci tot aan 1000 printen.

# Oplossing 1: Wisselen van variabelen met behulp van komma.
###############################################################################################################
getal1 = 0
getal2 = 1
fibonacci_reeks = []

# Volgende Fibonacci-getal berekenen, toevoegen aan de lijst en printen.
while getal2 <= 1000:
    getal1, getal2 = getal2, getal1 + getal2

    fibonacci_reeks.append(getal1)
    print(getal1)


# Oplossing 2: Oplossen zonder komma.
###############################################################################################################
getal1 = 0
getal2 = 1
fibonacci_reeks = []

# Volgende Fibonacci-getal berekenen, toevoegen aan de lijst en printen.
while getal2 <= 1000:
    tijdelijk_getal = getal1
    getal1 = getal2
    getal2 = tijdelijk_getal + getal1
    fibonacci_reeks.append(getal1)
    print(getal1)