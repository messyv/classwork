a = int(input("Háromszög első oldala:"))
b = int(input("Háromszög második oldala:"))
c = int(input("Háromszög harmadik oldala:"))

if a+b > c and b+c >a and a+c > b:
	print("A háromszög szerkeszthető.")
else:
	print("A háromszög nem szerkeszthető.")

if (a**2)+(b**2) == c**2 or (a**2) + (c**2) == (b**2) or (b**2) + (c**2) == a**2:
	print ("A háromszög derékszögű.")
else:
	print("A háromszög nem derékszögű.")
