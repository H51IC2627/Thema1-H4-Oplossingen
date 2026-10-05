# Grootste getal: Een functie die het grootste getal van twee getallen vindt.

def max_getallen(getal1, getal2):
    """
        Geeft het grootste getal terug.
        Argumenten:
            getal1 (integer)
            getal2 (integer)
        Returns:
            grootste getal (integer)
    """
    if getal1 > getal2:
        return getal1
    else:
        return getal2

# Functie oproepen voor 3 getallenparen.
print(max_getallen(5, 10))
print(max_getallen(20, 8))
print(max_getallen(5, 5))