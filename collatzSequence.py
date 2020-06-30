print('Enter a number: ')
number = int(input())

def collatz(number):
	if number == 1:
		print(int(number))
	elif number % 2 == 0:
		print(int(number))
		even = number / 2
		collatz(even)
	elif number % 2 == 1:
		print(int(number))
		odd = 3 * number + 1
		collatz(odd)

collatz(number)