print('-------------------------------------------------------------------')
print('2. Write a Python program to reverse a word after accepting the input from the user.')
strval = input('Enter string: ')
l = len(strval) - 1

revstrval = ''
while l >= 0:
    revstrval += strval[l]
    l -= 1       
print(revstrval)