#from itertools import combinations
list_num=[1,5]
n=4
condition=True
while condition:
    num=n*(3*n-1)//2
    for i in list_num:
        p=i+num
        if (((p*24+1)**0.5)+1)%6==0.0:
             #q=abs(i[0]-i[1])
             q=abs(i-num)
             if (((q*24+1)**0.5)+1)%6==0.0:
                 print(q)
                 condition=False
    
                
    list_num.append(num)
    n+=1
             
    
