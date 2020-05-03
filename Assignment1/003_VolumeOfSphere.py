import math

print('3. Volume of sphere')
diameter = int(input('Enter diameter of the sphere: '))
rad = diameter / 2
v = (4/3) * math.pi * (rad ** 3)
print('The volume of sphere is: ' + str(v))