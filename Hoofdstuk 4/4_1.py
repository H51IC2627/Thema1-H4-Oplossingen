# Getal controleren: functie die controleert of een getal (on)even is.

def is_even(getal):
    """
        Controleert of getal even/oneven is.
        argumenten: 
            getal (integer)
        returns: 
            getal even (True)/ getal oneven (False)
    """
    if getal % 2 == 0:
        return True
    else:
        return False

# Functie oproepen voor het getal 4 en 7
print(is_even(4))
print(is_even(7))