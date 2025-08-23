class employee:
    salary = 120000
    language = "Python"


    def getinfo(self):
        print(f"this is my salary = {self.salary}. and language is {self.language}.")

    @staticmethod    
    def greet():
        print("good morning")    

vashu = employee()
vashu.getinfo()

vashu.greet()