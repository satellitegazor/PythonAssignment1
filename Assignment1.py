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
print('-------------------------------------------------------------------')
print('2. Accept FirstName and LastName, add space in between first and last name and print in reverse')
firstname = input('Enter First Name: ')
lastname = input('Enter Last Name: ')

fullname = firstname + ' ' + lastname
l = len(fullname) - 1

revfullname = ''
while l >= 0:
    revfullname += fullname[l]
    l -= 1       
print(revfullname)
print('-------------------------------------------------------------------')
print('3. Volume of sphere')
diameter = int(input('Enter diameter of the sphere: '))
rad = diameter / 2
v = (4/3) * math.pi * (rad ** 3)
print('The volume of sphere is: ' + str(v))