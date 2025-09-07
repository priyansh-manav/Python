print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
a = int(input("Enter your number for A : "))
b = int(input("Enter your number for B : "))
print("Chose Add = '+', Sub = '-' , Multi = '*' , Divide = '/' , Rem = '%' ")
cal = input("Enter for Calculation : ")

dist1 = {
    "+" : 1,
    "-" : 2,
    "*" : 3,
    "/" : 4,
    "%" : 5
}

print(f"Value of A = {a}")
print(f"Value of B = {b}")

if(dist1[cal] == 1):
    print(f"A + B = {a+b}")
elif(dist1[cal] == 2):
    print(f"A - B = {a-b}")    
elif(dist1[cal] == 3):
    print(f"A * B = {a*b}")    
elif(dist1[cal] == 4):
    print(f"A / B = {a/b}")    
elif(dist1[cal] == 5):
    print(f"A % B = {a%b}")
else:
    print("Invalid input!")    