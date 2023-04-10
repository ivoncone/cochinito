import random

# dummy database of days already put in cochinito
ahorros = [1, 7, 11, 13, 14, 15, 16, 18, 20, 22, 24, 29, 30, 33, 35, 37, 39, 40, 41, 42, 43, 44, 46, 50, 53, 55, 61, 65, 66, 68, 69, 72, 74, 75, 79, 80, 81, 82, 83, 89, 90, 91, 92
 		]
total = sum(ahorros)

def main():

	#user_input = (input('¿User cuantos días quieres ahorrar?:   '))
	# convert input to integer
	#saving_days = int(user_input)
	saving_days = 100

	# return range of selection days
	day_selection = range(1, saving_days)
	
	# covert day_selection in a list
	days = list(day_selection)

	number = [n for n in days]
	random_num  = random.choice(number)
	while True:
		if random_num not in ahorros:
			print("Hoy tienes que poner en el cochinito:  $" + str(random_num))
			print("Hasta hoy has ahorrado:  $" + str(total))
			break
		else:
			print("Ya has completado tus dias de ahorro... Tu cochinito esta lleno")
			break

if __name__ == '__main__':
	main()
