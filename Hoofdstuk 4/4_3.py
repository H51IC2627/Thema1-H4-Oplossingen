# Politiecontrole: Een functie die bepaalt of je met de auto mag rijden.

def politiecontrole_uitvoeren(leeftijd, rijbewijs):
    """
        Controleert of je een geldige chauffeur bent. 
        Je moet een rijbewijs hebben en minstens 18 jaar zijn.
        Argumenten:
            leeftijd (integer)
            rijbewijs (boolean)
        Returns:
            Geldige chauffeur / Geen geldige chauffeur (string)
    """
    if leeftijd >= 18 and rijbewijs:
        return "Geldige chauffeur"
    else:
        return "Geen geldige chauffeur"

# Functie oproepen voor 3 chauffeurs.
print(politiecontrole_uitvoeren(20, True))
print(politiecontrole_uitvoeren(17, True))
print(politiecontrole_uitvoeren(20, False))