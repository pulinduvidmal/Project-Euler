listn=[1,2,3,4,5,6,7,8,9]
max_num=0

def f(i):
    n=1
    global k
    k=""
    while True:
        p=i*n
        l=str(p)
        for j in l:     
            if int(j) in list1:
                return list1    
        else:
            for j in l:
                list1.append(int(j))
        k=k+l
        n+=1
        
for i in range(50000,2,-1):
    list1=[]
    x=f(i)
    x.sort()
    if x==listn:
        if int(k)>max_num:
            max_num=int(k)
print(max_num)

