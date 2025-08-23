def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n


n = int(input("Enter the number : "))

print(f"Sums of the number is {sum(n)}")