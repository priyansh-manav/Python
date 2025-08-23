class Demo:
    a = 4



b = Demo()
print(b.a) # Prints the class attribute because instance attribute is not present
b.a = 16  # Instance attribute is set
print(b.a) # Prints the instance attribute because instance attribute is present



print(Demo.a) # Prints the class attribute 