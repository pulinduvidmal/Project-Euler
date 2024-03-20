i=1
while True:
    sum=0
    for j in range(1,i+1):
        sum+=j
    list1=[]
    for k in range(2,int(sum**0.5)+1):
        if sum%k==0:
            list1.append(k)
    print(sum,"     ",list1)
    if len(list1)>249:
        break
    i+=1


