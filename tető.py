hossz = 2300
szélesség = 960
magasság = 320
másikoldal = szélesség/2

import math
tetőrövidebboldala = float(math.sqrt((magasság**2)*(másikoldal**2)))
print ("tető rövidebb oldala:", tetőrövidebboldala)

tetőterület = 2*(tetőrövidebboldala*hossz)
print ("Tető területe:", tetőterület)

cserépterület = 25*12
mennyiség = tetőterület/cserépterület

print( "Szükséges cserép db:", mennyiség)


