class calculator:
    def __init__(self,n):
        self.n = n
    def square(self):
        print(f"This is a square of a number = {self.n*self.n}")   
    def cube(self):
        print(f"This is a cube of a number = {self.n*self.n*self.n}")   
    def squareroot(self):
        print(f"This is a squareroot of a number = {self.n**1/2}")



num = calculator(4)
num.square()
num.cube()
num.squareroot()
