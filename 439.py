testsuly = float(input("Testsúly:"))
magassag = float(input("Magasság:"))
kor = float(input("Kor:"))
sport = input("Sportol? (Igen/Nem)")

	

def normal():
	
	tmi = 1.3*testsuly / magassag**2.5
	
	print("Testtömegindex:", tmi)
	
	if tmi < 16:
		print("Súlyos soványság.")
	
	if tmi > 16 and tmi < 16.9:
		print("Mérsékelt soványság.")

	if tmi > 17 and tmi < 18.49:
		print("Enyhe soványság.")

	if tmi > 18.5 and tmi < 24.9:
		print("Egészséges.")
	
	if tmi > 25 and tmi < 29.9:
		print("Túlsúlyos.")
	
	if tmi > 30 and tmi < 34.9:
		print ("I. fokú elhízás")

	if tmi > 35 and tmi < 39.9:
		print ("II. fokú elhízás.")
	
	if tmi > 40:
		print("III.fokú elhízás.")
	
def idos_sport():
	
	tmi = 1.3*testsuly / magassag**2.5
	
	print("Testtömegindex:", tmi)
	
	if tmi < 16:
		print("Súlyos soványság.")
	
	if tmi > 16 and tmi < 16.9:
		print("Mérsékelt soványság.")

	if tmi > 17 and tmi < 18.49:
		print("Enyhe soványság.")

	if tmi > 18.5 and tmi < 27:
		print("Egészséges.")
	
	if tmi > 27.1 and tmi < 29.9:
		print("Túlsúlyos.")
	
	if tmi > 30 and tmi < 34.9:
		print ("I. fokú elhízás")

	if tmi > 35 and tmi < 39.9:
		print ("II. fokú elhízás.")
	
	if tmi > 40:
		print("III.fokú elhízás.")
	
def pubertas():
	tmi = 1.3*testsuly / magassag**2
	
	print("Testtömegindex:", tmi)
	
	if tmi < 16:
		print("Súlyos soványság.")
	
	if tmi > 16 and tmi < 16.9:
		print("Mérsékelt soványság.")

	if tmi > 17 and tmi < 18.49:
		print("Enyhe soványság.")

	if tmi > 18.5 and tmi < 24.9:
		print("Egészséges.")
	
	if tmi > 25 and tmi < 29.9:
		print("Túlsúlyos.")
	
	if tmi > 30 and tmi < 34.9:
		print ("I. fokú elhízás")

	if tmi > 35 and tmi < 39.9:
		print ("II. fokú elhízás.")
	
	if tmi > 40:
		print("III.fokú elhízás.")
	
def csecsemo():
	tmi = 1.3*testsuly / magassag**3
	
	print("Testtömegindex:", tmi)
	
	if tmi < 16:
		print("Súlyos soványság.")
	
	if tmi > 16 and tmi < 16.9:
		print("Mérsékelt soványság.")

	if tmi > 17 and tmi < 18.49:
		print("Enyhe soványság.")

	if tmi > 18.5 and tmi < 24.9:
		print("Egészséges.")
	
	if tmi > 25 and tmi < 29.9:
		print("Túlsúlyos.")
	
	if tmi > 30 and tmi < 34.9:
		print ("I. fokú elhízás")

	if tmi > 35 and tmi < 39.9:
		print ("II. fokú elhízás.")
	
	if tmi > 40:
		print("III.fokú elhízás.")
	
if sport == "Igen" or kor == 50:
	idos_sport()

	
if kor > 12 and kor < 19:
	pubertas()

if kor < 0.5:
	csecsemo()

if kor > 0.6 and kor < 12 and kor > 19 and not kor == 50:
	normal()
