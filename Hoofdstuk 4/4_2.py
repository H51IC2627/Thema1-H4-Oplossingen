# Bereken korting: Functie die de prijs na korting bepaalt.

def korting_bepalen(prijs, korting):
    """
        Bepaalt de prijs na korting.
        Argumenten:
            prijs (integer)
            korting percentage (integer)
        Returns:
            Prijs na korting (float)
    """
    return prijs - prijs * korting / 100

# Resultaat van korting_bepalen printen voor 10% van 100 euro en 20% van 50 euro
print(korting_bepalen(100, 10))
print(korting_bepalen(50, 20))