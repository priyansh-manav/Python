maths = int(input("Enter the number of maths : "))
english = int(input("Enter the number of english : "))
bio = int(input("Enter the number of bio : "))

total_percentage = (100*(maths+english+bio))/300
if(total_percentage>=40 and maths>=33 and english>=33 and bio>=33):
    print("You are Pass :",total_percentage)
else:
    print("You are Fail :",total_percentage)    