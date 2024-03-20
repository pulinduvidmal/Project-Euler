import time
sum1=0
start=time.time()
for i in range(2,1000000):
    sum=0
    for j in (str(i)):
        sum+=(int(j))**5

    if sum==i:
        print(i)
        sum1+=i
end=time.time()
print(end-start)
print(sum1)
