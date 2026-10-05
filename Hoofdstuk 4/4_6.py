# Driehoek checker: Controleert of drie zijden een geldige driehoek vormen.

def is_geldige_driehoek(zijde1, zijde2, zijde3):
    """
        Bepaalt of drie zijden een geldige driehoek vormen.
        zijde1 + zijde2 > zijde3 en alle zijdes > 0
        Argumenten:
            zijde1 (integer)
            zijde2 (integer)
            zijde3 (integer)
        Returns:
            Geldige driehoek (True)/ongeldige driehoek (False)
    """ 
    if not(zijde1 == 0 or zijde2 == 0 or zijde2 == 0):
        if zijde1 + zijde2 > zijde3:
            return True
        else:
            return False
    else:
        return False

# Functie oproepen voor 3 driehoeken
print(is_geldige_driehoek(3, 4, 5))
print(is_geldige_driehoek(1, 2, 10))
print(is_geldige_driehoek(0, 5, 5))