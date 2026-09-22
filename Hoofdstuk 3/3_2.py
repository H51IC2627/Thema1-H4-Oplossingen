# Rapportbeoordeling: Rapportcijfer omzetten naar een beoordeling (onvoldoende, matig, voldoende, goed en uitstekend)

rapportcijfer = int(input("Welk cijfer moet ik beoordelen? "))

# Beoordeling instellen opbv cijfer.
if rapportcijfer <= 3:
    beoordeling = "onvoldoende"
elif rapportcijfer <= 5:
    beoordeling = "matig"
elif rapportcijfer <= 7:
    beoordeling = "voldoende"
elif rapportcijfer <= 9:
    beoordeling = "goed"
else:
    beoordeling = "uitstekend"

print("Beoordeling: " + beoordeling)