a = int(input("Enter a number 1st : "))
b = int(input("Enter a number 2nd : "))
c = int(input("Enter a number 3rd : "))

def largest_number():
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c


print(f"Largest number is {largest_number()}")
