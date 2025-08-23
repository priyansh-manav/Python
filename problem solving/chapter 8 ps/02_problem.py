
def temp(f):
    return 5*(f-32)/9

f = int(input("Enter temperatur in F : "))
c = temp(f)

print(f"Temperature in Calcius {round(c,2)}")