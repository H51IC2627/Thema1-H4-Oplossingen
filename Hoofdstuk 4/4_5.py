# Kaartwaarde: Functie die de waarde van een speelkaart bepaalt
def kaartwaarde_bepalen(kaart):
    """
        Kaartwaarde van kaart bepalen.
        Argumenten:
            kaart (string)
        Returns:
            kaartwaarde (integer)
    """
    if kaart == "J" or kaart == "Q" or kaart == "K":
        return "10"
    elif kaart == "A":
        return "11"
    else:
        return kaart

# Functie oproepen voor 3 kaarten
print(kaartwaarde_bepalen("5"))
print(kaartwaarde_bepalen("K"))
print(kaartwaarde_bepalen("A"))