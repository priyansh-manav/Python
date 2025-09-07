def Fact(num):
    if(num == 0 or num == 1):
        return 1
    else:
        return num*Fact(num-1)
    

num = int(input("Enter number for Factorial: "))
factorial = Fact(num)
print(f"The Factorial of number = {factorial}")    