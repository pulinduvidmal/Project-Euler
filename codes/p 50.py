import time
start=time.time()
sum1=0

lk=0
list1=[]
h=1000000
def f(x):
    kn=True
    for i in range(2,int((x**0.5)+1)):
        if x%i==0:
            kn=False
            break                      
    if kn:
        return True
    
for x in range(2,h//2):
    if f(x):
        list1.append(x)
        
        sum1+=x   
m=0
pre=1
print(list1[-1])
while m<len(list1)//2:
    sum3=0
    list2=[]        
    for k in range(m,len(list1)//2):        
        sum3+=list1[k]
        list2.append(list1[k])
                
        if sum3<h and f(sum3)==True:
            if pre<len(list2):
                pre=len(list2)
                mx=sum3                                
    m+=1
end=time.time()
print(mx)
print(pre)
print("time is",end-start)
    

            
    


        

    
    
