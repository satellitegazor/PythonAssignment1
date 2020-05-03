class BaseClass:
    
    a = 0
    b = 0
    c = 0
    def TakeInput(self):
        self.a = int(input("Enter length of side A: "))
        self.b = int(input("Enter length of side B: "))
        self.c = int(input("Enter length of side C: "))

class DerivedClass(BaseClass):

    def CalcTriangleArea(self):
        s = (self.a + self.b + self.c) / 2
        self.area = (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

        print("The area of the triangle with sides {}, {}, {} is {}".format(self.a, self.b, self.c, self.area))

d = DerivedClass()
d.TakeInput()
d.CalcTriangleArea()

#output
#Enter length of side A: 4
#Enter length of side B: 5
#Enter length of side C: 6
#The area of the triangle with sides 4, 5, 6 is 9.921567416492215
