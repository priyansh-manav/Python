a = int(input("Enter your 1st number : "))
b = int(input("Enter your 2nd number : "))
c = int(input("Enter your 3rd number : "))


if(a>b and a>c):
    print(f"1st number is a greatest number : {a}")
elif(b>a and b>c):
    print(f"2nd number is a greatest number : {b}")
else:
    print(f"3rd number is a greatest number : {c}")       