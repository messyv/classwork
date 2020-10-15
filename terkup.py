#Szitás-Kiss Vanda
print("Ez a program egy kúp adatait kéri be majd területét számolja ki.")
sugár = float(input("Sugár:"))
magasság = float(input("Magasság:"))

import math

terület = (((sugár**2 *math.pi)/3)*magasság)
print("Kúp területe=", terület)
