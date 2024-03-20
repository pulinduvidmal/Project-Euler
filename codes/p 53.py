def f(x):
    if x==0:
        return 1
    return x*f(x-1)
count=0
for i in range(1,101):
    for j in range(0,i):
        value=f(i)/(f(j)*f(i-j))
        if value>1000000:
            count+=1
print(count)
