
szomjas = 0
ehezes = 0
cmd = ''
while cmd != 'vége':
	cmd = input("Tamagochi:")
	ehezes += 1
	if cmd == 'etet':
		ehezes -= 7
	if ehezes > 7:
		print("Éhezem!")
	szomjas += 1
	if cmd == 'itat':
		szomjas -= 7
	if szomjas > 7:
		print("Szomjazom!")
	if ehezes > 10:
		print("Meghaltam.")
		cmd = 'vége'
