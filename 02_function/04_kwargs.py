def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")



print_kwargs(name= "Vishakha",age = 20 , status = "Best friend")
print_kwargs(name= "Vashu",age= 20, vishkhas = "Best friend")        