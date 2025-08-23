age = int(input("Enter your age : "))
if(age>=18):
    print("You are above the age of consent")
    print("congrats!!")

elif(age<0):
    print("You are entering a invalid negative number!")

elif(age==0):
    print("You are entering 0 which is not a valid age!")    

else:
    print("You are below the age of consent")

print("End of program!!")        