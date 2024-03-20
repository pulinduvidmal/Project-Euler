
def f(x):
    if x==2:
        return True
    if x%2==0:
        return False
    for i in range(3,int(x**0.5)+1,2):
        if x%i==0:
            return False
    return True
p,q=0,0
import time
start=time.time()
maxprime_count=0
for a in range(-999,1000):
    for b in range(-999,1000):
        n=0
        count=0
        while True:
            if f(abs((n**2)+(a*n)+b)):
                count+=1
            else:
                break
            n+=1
        if count>maxprime_count:
            maxprime_count=count
            p,q=a,b
end=time.time()
print("a",p,"b",q,"a*b",p*q)        
print("time is",end-start) 
