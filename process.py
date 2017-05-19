import csv


with open('areas.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	print('Northern Cape:{')
	for row in spamreader:
		if row[1] == 'Northern Cape':
			print("'"+row[0]+"'" + ',')
	print('}')

with open('areas.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	print('Eastern Cape:{')
	for row in spamreader:
		if row[1] == 'Eastern Cape':
			print("'"+row[0]+"'" + ',')
	print('}')

with open('areas.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	print('Limpopo:{')
	for row in spamreader:	
		if row[1] == 'Limpopo':
			print("'"+row[0]+"'" + ',')
	print('}')

with open('areas.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	print('KwaZulu-Natal:{')
	for row in spamreader:
		if row[1] == 'KwaZulu-Natal':
			print("'"+row[0]+"'" + ',')
	print('}')

with open('areas.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	print('Gauteng:{')
	for row in spamreader:
		if row[1] == 'Gauteng':
			print("'"+row[0]+"'" + ',')
	print('}')

with open('areas.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	print('Western Cape:{')
	for row in spamreader:
		if row[1] == 'Western Cape':
			print("'"+row[0]+"'" + ',')
	print('}')

with open('areas.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	print('Mpumalanga:{')
	for row in spamreader:
		if row[1] == 'Mpumalanga':
			print("'"+row[0]+"'" + ',')
	print('}')

with open('areas.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	print('North West:{')
	for row in spamreader:
		if row[1] == 'North West':
			print("'"+row[0]+"'" + ',')
	print('}')

with open('areas.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	print('Free State:{')
	for row in spamreader:
		if row[1] == 'Free State':
			print("'"+row[0]+"'" + ',')
	print('}')



#'Northern Cape'
#'Eastern Cape'
#'Limpopo'
#'KwaZulu-Natal'
#'Gauteng'
#'Western Cape'
#'Mpumalanga'
#'Free State'
#'North West'