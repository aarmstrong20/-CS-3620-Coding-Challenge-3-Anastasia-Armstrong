#override * to behave like +

class Num:
    def __init__(self, x):
        self.x = x
    def __mul__(self, other):
        return Num(self.x + other.x)
    def __add__(self, other):
        return Num(self.x + other.x)
    def __str__(self):
        return str(self.x)


a = Num(1)
b = Num(2)
print(a+b)
print(a*b)