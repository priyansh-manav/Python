class employee:
    a = 16
    
    @classmethod
    def show(cls):
        print(f"The class attribute value of a = {cls.a}")



b = employee()
b.a = 15
b.show()        