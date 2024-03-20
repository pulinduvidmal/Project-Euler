n=2
l=3
b=l**2
a=3
    
def f(x):
    if x==2:
        return True
    if x%2==0:
        return False
    for i in range(3,int(x**0.5)+1,2):
        if x%i==0:
            return False
    return True

#list1=[1]
v=5
count=0
while True:
    

    for k in range(a,b,n):
        if f(k):
            count+=1
    if (count/v)<(1/10):
        print(l)
        break
    
    #print(l,count,v)   
    a=b
    l+=2
    b=l**2
    n+=2
    v+=4
    

