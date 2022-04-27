# Find the Square , SqaureRoot and Cube of a Given Number

class Calculator:
    def __init__(self,num):
        self.num = num

    def square(self):
        print(f"The Square of {self.num} is {self.num **2}")
    
    def squareRoot(self):
        print(f"The SquareRot of {self.num} is {self.num **0.5}")

    def cube(self):
        print(f"The Cube of {self.num} is {self.num **3}")

a = Calculator(9)

a.square()
a.squareRoot()
a.cube()