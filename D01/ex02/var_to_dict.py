def list_to_dict(liste):
	my_dict = dict()
	for var in liste:
		if var[1] in my_dict:
			my_dict[var[1]].append(var[0])
		else:
			my_dict[var[1]] = [var[0]]
	for key in my_dict:
		print(key, ":", end = '')
		for value in my_dict[key]:
			print('', value, end= '')
		print()

def create_list():
    d = [
	('Hendrix' , '1942'),
	('Allman' , '1946'),
	('King' , '1925'),
	('Clapton' , '1945'),
	('Johnson' , '1911'),
	('Berry' , '1926'),
	('Vaughan' , '1954'),
	('Cooder' , '1947'),
	('Page' , '1944'),
	('Richards' , '1943'),
	('Hammett' , '1962'),
	('Cobain' , '1967'),
	('Garcia' , '1942'),
	('Beck' , '1944'),
	('Santana' , '1947'),
	('Ramone' , '1948'),
	('White' , '1975'),
	('Frusciante', '1970'),
	('Thompson' , '1949'),
	('Burton' , '1939')
	]
    return d

if __name__ == '__main__':
    list_to_dict(create_list())