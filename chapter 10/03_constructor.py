class employe:
    salary = 120000
    language = "Python"
    
    def __init__(self):  # dhunder method which is autommatically called
        print("I am creating an object")


    def getinfo(self):
        print(f"The language is {self.language}, and the salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("Good Morning!")




vashu = employe()
vashu.greet()
vashu.name = "Priyansh"
print(vashu.salary, vashu.language, vashu.name)            