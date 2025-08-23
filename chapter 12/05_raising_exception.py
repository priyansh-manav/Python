a = int(input("Enter a number :" ))
b = int(input("Enter second number : "))

if(b == 0):
    raise ZeroDivisionError("hey our program is not meant to divide numbers bby zero ")
else:
    print(f"The division a/b is{a/b}")