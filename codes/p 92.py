i=2
count=0
import time
start=time.time()
while i<10000000:
    p = i
    while True:
        x = 0
        for j in str(p):
            x += int(j) ** 2
        p=x
        if p==1 or p==10:
            break
        if p == 89:
            print(i)
            count += 1
            break

    i+=1
end=time.time()
print("count-",count)
print(end-start)