import math

cena = float(input("Ievadīt linoleja cenu (EUR/m^2): "))
Rplatums = float(input("Ievadīt linoleja ruļļa platumu: "))
Tplatums = float(input("Ievadīt telpas platumu: "))
Tgarums = float(input("Ievadīt telpas garumu: "))

rulli = math.ceil(Tgarums / Rplatums)
Tizmers = math.ceil(Tplatums * Tgarums)
cena2 = (Tizmers * cena / rulli)

print(cena2)