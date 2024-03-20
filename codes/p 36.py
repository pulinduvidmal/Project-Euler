def f(n):  
    if len(str(n))%2==0:       
        x=str(n)[:(len(str(n)))//2]
        y=str(n)[(len(str(n)))//2:]
        p=""
        for i in x:
            p=i+p
        if y==p:          
            p=2
            return p           
    else:
        x=str(n)[:(len(str(n)))//2]
        y=str(n)[(len(str(n)))//2+1:]
        p=""
        for i in x:
            p=i+p
        if y==p:
             p=2
            #print(n,p)
             return p           
sum1=0
for i in range(1,1000000):
    list1=[]
    list2=[]
   
    h=int(bin(i)[2:])
    #print(i,h)
    p=5
    f(i)
    
    if f(i)==2 and f(h)==2:
        sum1+=i
        print(i,"   ",h)        
print("sum is",sum1)    
        
    
        
    







    
        
        
