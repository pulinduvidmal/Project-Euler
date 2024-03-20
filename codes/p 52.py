def f(x):
    list_num=[]
    for i in str(x):
        list_num.append(int(i))
    list_num.sort()
    return list_num
        

n=10
while True:
    for i in range(2,7):
        if f(n*i)!=f(n):
            break
    else:
        print(n)
        break
    n+=1
    
