def f(x):
    if x==1:
        return True
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return True
    return False


n=3

condition=True
while condition:
    if f(n):
        for j in range(1,n,2):
            if f(j)==False:
                if (((n-j)//2)**0.5)%1==0.0:
                    break
        else:
            print(n)
            condition=False
    
    n+=2
