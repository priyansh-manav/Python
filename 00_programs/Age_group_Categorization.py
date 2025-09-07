# Age group Categorization

age = int(input("Enter your age: "))

if(age>=60):
    print("Senior")
elif(age>=20 and age<=59):
    print("Adult")
elif(age>=13 and age<=19):
    print("Teenager")
elif(age<13):
    print("Child")
else:
    print("Invalid age!")            