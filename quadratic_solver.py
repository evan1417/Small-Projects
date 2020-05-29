#! usr/bin/env python3

a = float(input('Please enter the a value of the equation:'))
b = float(input('Please enter the b value of the equation:'))
c = float(input('Please enter the c value of the equation:'))

def quadratic(a,b,c):
	'''
	This function will solve for x using the quadratic formula 
	INPUT: The values for a,b, and c
	OUTPUT: The x intercept(s) associating the coefficients
	'''
	if a == 0:
		print('This value cannot equal 0')
	result1 = ((-b)+(((b**2) - (4*a*c))**0.5))/(2*a)
	result2 = ((-b)-(((b**2) - (4*a*c))**0.5))/(2*a)
	if result1 == result2:
		print('The x intercept is ' + str(result1))
	else:
		print('The x-intercepts are ' + str(result1) + ' and ' + str(result2))
	  
print(quadratic(a,b,c))