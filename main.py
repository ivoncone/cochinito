import random

# dummy database of days already put in cochinito
ahorros = [16, 29, 30, 35, 37, 39, 40, 41, 44, 50, 53, 69, 82, 83, 90, 91
 		]
total = sum(ahorros)

def main():
	user_input = (input('¿User cuantos días quieres ahorrar?:   '))
	# convert input to integer
	saving_days = int(user_input)

	# return range of selection days
	day_selection = range(1, saving_days)
	
	# covert day_selection in a list
	days = list(day_selection)

	number = [n for n in days]
	while number not in ahorros:
		random_num  = random.choice(number)
		print("Hoy tienes que poner en el cochinito:  $" + str(random_num))
		break
	
	print("Hasta hoy has ahorrado:  $" + str(total))

if __name__ == '__main__':
	main()
