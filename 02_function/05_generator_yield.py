def even_num(limit):
    for i in range(2,limit+1,2):
        yield i



for j in even_num(10):
    print(j)