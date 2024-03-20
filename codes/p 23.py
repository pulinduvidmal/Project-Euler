def f(x):    
    sum_i=0
    for j in range(1,(x//2)+1):        
        if x%j==0:
            sum_i+=j
    return sum_i


import time
start=time.time()

list_num=[i for i in range(1,28123) if f(i)>i]

list_num=list(set(list_num))

#print(list_num)
list_k=[]
for i in list_num:
    for j in list_num[list_num.index(i):]:
        list_k.append(i+j)

list_k=list(set(list_k))

notsum=0
for i in range(1,28123):
    if i not in list_k:
        notsum+=i        

print(notsum)
end=time.time()
print("time is",end-start)

#print(list_k)

        
    
