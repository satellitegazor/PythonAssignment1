print('Python Assignment 2')
print('-------------------------------------------------------------------')
print('1. Create the below pattern using nested for loop in Python.')

i = 0
star = ''
for i in range(0, 2):
    if i == 0:
        for g in range(0, 5):
            star += '*'
            print(star)            
    if i == 1:
        for s in range(4, 0, -1):
            ##k = star[0, s]
            ##print(k)
            print(star[:s])
    
    
print('-------------------------------------------------------------------')
print('2. Write a Python program to reverse a word after accepting the input from the user.')
strval = input('Enter string: ')
l = len(strval) - 1

revstrval = ''
while l >= 0:
    revstrval += strval[l]
    l -= 1       
print(revstrval)