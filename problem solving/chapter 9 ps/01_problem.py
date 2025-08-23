f = open("poem.txt")
data = f.read()
if("twinkle" in data):
    print("The word twinkle is present in the data")
else:
    print("The word twinkle is not present in the data")    
f.close()