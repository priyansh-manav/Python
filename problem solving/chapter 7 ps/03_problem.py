n = int(input("Enter number : "))

for i in range(2,n):
    if((n%i)==0):
        print("Number is not a prime number")
        break
else:
    print("Number is a prime number")    
