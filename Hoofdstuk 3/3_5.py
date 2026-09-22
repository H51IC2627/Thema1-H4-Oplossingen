# Wachtwoordchecker: Controleert of een wachtwoord sterk is.

wachtwoord = input("Geef een wachtwoord. ")

# Initialisatie van sterkte (aan hoeveel voorwaarden voldoet het wachtwoord?) en soorten (welke soorten elementen bevat het wachtwoord?)
sterkte = 0
soorten = ""

# Controleren op letters
if "a" in wachtwoord or "b" in wachtwoord or "c" in wachtwoord or \
   "d" in wachtwoord or "e" in wachtwoord or "f" in wachtwoord or \
   "g" in wachtwoord or "h" in wachtwoord or "i" in wachtwoord or \
   "j" in wachtwoord or "k" in wachtwoord or "l" in wachtwoord or \
   "m" in wachtwoord or "n" in wachtwoord or "o" in wachtwoord or \
   "p" in wachtwoord or "q" in wachtwoord or "r" in wachtwoord or \
   "s" in wachtwoord or "t" in wachtwoord or "u" in wachtwoord or \
   "v" in wachtwoord or "w" in wachtwoord or "x" in wachtwoord or \
   "y" in wachtwoord or "z" in wachtwoord:
    sterkte += 1
    soorten += "letters "

# Controleren op cijfers
if "0" in wachtwoord or "1" in wachtwoord or "2" in wachtwoord or \
   "3" in wachtwoord or "4" in wachtwoord or "5" in wachtwoord or \
   "6" in wachtwoord or "7" in wachtwoord or "8" in wachtwoord or \
   "9" in wachtwoord:
    sterkte += 1
    soorten += "cijfers "

# Controleren op speciale symbolen
if "!" in wachtwoord or "@" in wachtwoord or "#" in wachtwoord or \
   "$" in wachtwoord or "%" in wachtwoord or "^" in wachtwoord or \
   "&" in wachtwoord or "*" in wachtwoord:
    sterkte += 1
    soorten += "speciale symbolen"

print("Het wachtwoord bevat: " + soorten + ".")

# Wachtwoord beoordelen
if sterkte <= 1:
    wachtwoord_beoordeling = "zwak"
elif sterkte <= 2:
    wachtwoord_beoordeling = "gemiddeld"
else:
    wachtwoord_beoordeling = "sterk"

print("Dit wachtwoord is " + wachtwoord_beoordeling + ".")