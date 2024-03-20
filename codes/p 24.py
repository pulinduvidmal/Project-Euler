def f(x):
    if x==1:
        
        return 1
    else:
        return x*f(x-1)

sum1=1000000
k=9
b=0
a=9

list2=[0,1,2,3,4,5,6,7,8,9]
list3=[]
while True:
    
    if sum1-f(k)>=0:
        b+=1
        sum1=sum1-f(k)
        if sum1==0:
            
            print("kk")
            list3.append(list2[b])
            del(list2[b])
            break
            

    else:
        k=k-1
        a-=1
        
        list3.append(list2[b])
        del(list2[b])
        b=0
    print("now sum is",sum1,"    ",a,b)

x=""
for i in list3+list2:
    x=x+str(i)
print("previous eka",int(x))
