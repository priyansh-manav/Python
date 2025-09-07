sum = 0
while(True):
    userinput = input("Enter your item price and q for quit:\n ")
    if(userinput != 'q'):
        sum = sum + int(userinput)
        print(f"Your order so far {sum}")
    else:
        print(f"Your total price = {sum},\nThank you for shoping")
        break    