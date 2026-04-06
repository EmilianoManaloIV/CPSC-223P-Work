class triangle:
    number_of_sides = 3
    def __init__(self,/,*,a1,a2,a3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
    def check_angles(self):
        isValid: bool = False
        if (self.a1 + self.a2 + self.a3) == 180:
            isValid = True
        return isValid

x = triangle(a1=60,a2=60,a3=60)
print(x)
print(x.check_angles())
print(x.number_of_sides)

y = triangle(a1=90,a2=90,a3=90)
print(y)
print(y.check_angles())
print(y.number_of_sides)

