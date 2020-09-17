import random

szam1 = random.randrange( 6) + 1
print (szam1)

szam2 = random.randrange( 6) + 1
print (szam2)

szam3 = random.randrange( 6) + 1
print (szam3)

szam4 = random.randrange( 6) + 1
print (szam4)

szam5 = random.randrange( 6) + 1
print (szam5)

print (
	"| %6s" % "Gép:",
	"%d" % szam1,
	"%d" % szam2,
	"%d" % szam3,
	"%d" % szam4,
	"%d |" % szam5,
	)
