def floorToInt(s : str) -> int:
	try:
		return int(s)
	except ValueError:
		return 0
		
def priceToInt(s : str) -> float:
	kur = {
		'TL':1.0,
		'USD':3.8,
		'EUR':4.67
	}
	s = s.replace('.', '')
	for (cur, val) in kur.items():
		if s.find(cur) != -1:
			s = s.replace(' ' + cur, '')
			return float(s)*val
	raise ValueError()

def parseFile(f : str) -> list:
	l = []

	with open('database.txt', 'r') as f:
		while True:
			s = f.readline()
			if s == '':
				break
			s = s[:-1]
			home={}
			props = s.split(",")
			home['age']=int(props[0])
			if (props[1] != 'UNK'):
				home['coordinatex'] = float(props[1])
				home['coordinatey'] = float(props[2])
				off = 0
			else:
				home['coordinatex'] = 0
				home['coordinatey'] = 0
				off = -1
			home['floor'] = floorToInt(props[3+off])
			if props[4+off].find('Ha') != -1:
				home['furnished'] = False
			else:
				home['furnished'] = True
			home['heating'] = props[5+off]
			home['location'] = props[6+off]
			home['m2'] = int(props[7+off][:-3].replace('.', ''))
			home['numrooms'] = props[8+off]
			home['price'] = priceToInt(props[9+off])
			l.append(home)
	return l
