a = int(input("Enter number for a : "))
b = int(input("Enter number for b : "))
c = int(input("Enter number for c : "))
d = int(input("Enter number for d : "))

if(a>b and a>c and a>d):
    print("A is a greatest number")
elif(b>a and b>c and b>d):
    print("B is a greatest number")
elif(c>a and c>b and c>d):
    print("C is a greatest number")
else:
    print("D is a greatest number")

