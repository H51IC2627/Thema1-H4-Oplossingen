# BMI-calculator: Bereken de BMI en geef gezondheidsadvies.

# Gewicht en lengte gebruiker vragen.
gewicht = int(input("Wat is jouw gewicht (kg)? "))
lengte = float(input("Hoe groot ben je (m)? "))

# BMI bepalen en tonen.
bmi = round(gewicht/(lengte*lengte), 1)
print("BMI: " + str(bmi))

# Gezondheidsadvies bepalen obv BMI.
if bmi < 18.5:
    advies = "ondergewicht"
elif bmi <= 24.9:
    advies = "een normaal gewicht"
else:
    advies = "overgewicht"

print("Je hebt " + advies + ".")