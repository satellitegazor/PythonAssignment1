import math 

print('Python Assignment 1')
print('-------------------------------------------------------------------')
print('1. Program to print number from 2000 to 3200 that are divisible by 7 but not by 5')
s = ''
for n1 in range(2000, 3201):
	notdivby5 = ((n1 % 5) != 0)
	divby7 = ((n1 % 7) == 0)
	if(divby7 and notdivby5):
		s += str(n1) + ', '
print(s)