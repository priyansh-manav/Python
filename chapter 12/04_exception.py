try:
    
    a = int(input("Enter your number : "))
    print(a)

except ValueError as v:
    print(v) 
    print("Thank you !")


except Exception as e:
    print(e)   
