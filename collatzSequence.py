print('Enter a number: ')
number = int(input()) # user should input a number

def collatz(number):
	'''
	This function will perform the collatz sequence on any number. 
	For even numbers, it merely halves the number. 
	For odd numbers it will perform the sequence (3 * odd number + 1) until the last number is equal to 1. 
	''' 
	
	if number == 1:
		print(int(number)) # once the number equals one the function loop stops 
	elif number % 2 == 0: # determines whether the input number is even 
		print(int(number))
		even = number / 2
		collatz(even)
	elif number % 2 == 1: # determines if the input number is odd 
		print(int(number))
		odd = 3 * number + 1
		collatz(odd)

collatz(number)
