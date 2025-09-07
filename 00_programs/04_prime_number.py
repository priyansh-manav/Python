num = int(input("Enter the number : "))
is_prime = True

if num > 0:
    for i in range(2,num):
        if(num%i) == 0:
            is_prime = False
            break

print(f"This number is a prime number : {is_prime}")        