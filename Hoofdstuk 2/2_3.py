origineel_bedrag = int(input("Hoeveel euro wil je omwisselen? "))
wisselkoers = float(input("Wat is de wisselkoers? "))
valuta = input("Naar welke valuta wissel je je geld? ")

nieuw_bedrag = origineel_bedrag * wisselkoers

print(str(origineel_bedrag) + " euro is " + str(nieuw_bedrag) + valuta)