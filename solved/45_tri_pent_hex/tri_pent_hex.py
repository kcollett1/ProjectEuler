t = 286
tria = 41041
p = 166
penta = 41251
h = 144
hexa = 41328

while True:
	while penta < tria:
		p += 1
		penta += (3*p - 2)
	if penta == tria:
		while hexa < tria:
			h += 1
			hexa += (4*h - 3)
		if hexa == tria:
			print t,h,p,tria
			break
	t += 1
	tria += t
