#Szitás-Kiss Vanda
print("Ez a program egy kúp adatait kéri be majd térfogatát számolja ki.")
sugár = float(input("Sugár:"))
magasság = float(input("Magasság:"))

import math

térfogat = (((sugár**2 *math.pi)*1/3)*magasság)
print("Kúp térfogata=", térfogat)
