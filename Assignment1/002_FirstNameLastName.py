import math 
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