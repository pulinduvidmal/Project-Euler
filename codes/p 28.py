n=2
l=3
b=l**2
a=3
    
sum1=1

#list1=[1]
p=1001
while True:

    for k in range(a,b,n):
        sum1+=k
        #list1.append(k)
    a=b
    l+=2
    b=l**2
    n+=2
    
    if a==p**2:
        break
print(sum1+(p**2))
