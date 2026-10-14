# Maaltafels: Print een maaltafel van 1 tot en met 10 voor een getal dat de gebruiker ingeeft.

getal = int(input("Welke maaltafel wil je krijgen? "))

# Maaltafel afgaan en printen.
for i in range(1, 11):
    print(str(getal) + " X " + str(i) + " = " + str(getal*i))