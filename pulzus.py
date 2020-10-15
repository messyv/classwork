#352-es feladat
#A program kiszámolja milyen pulzussal érdemes edzeni.

print("Kezdő edzés: 50% alatt")
print("Regeneráló edzés: 50-60%")
print("Zsírégető edzés: 60-70%")
print("Aerob kapacitás fejlesztése: 70-85%")
print("Anaerob állóképesség fejlesztés: 85-95%")
print("Gyorsaság, robbanékonyság fejlesztése: 95-100%")

életkor = float(input("Életkor:"))
nyugalmipulzus = float(input("Nyugalmi pulzus:"))
edzésszázalék = float(input("Milyen százalékos intenzitással szeretne edzeni:"))

maxpulzus = (220-életkor)
százalék = (maxpulzus*edzésszázalék)/100

pulzustartalék = maxpulzus - nyugalmipulzus
ajánlott = (pulzustartalék * edzésszázalék)+nyugalmipulzus

print(ajánlott, "%-kal ajánlott edzeni!")
