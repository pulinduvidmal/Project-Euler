def f(x):
    if x==1:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    else:

        return True





count=0
sum_num=0
n=10
#print(type(len(str(n))))
while True:
    if f(n)==True:
        for i in range (1,(len(str(n)))):
            l=int(str(n)[i:])
            k=int(str(n)[:-i])
            #print(l,k)
            if f(int(l))!=True or f(int(k))!=True :
                break
                             
                             
                             
        else:
            count+=1
            sum_num+=n
            print(n)
    if count==11:
        break
    n+=1
print("sum is ",sum_num)
    
        
        
    
    
