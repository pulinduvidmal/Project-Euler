count = 4
n = 10
while n < 1000000:
    isprime= True
    for j in range(2,int(n**0.5)+1):


        if n%j == 0:
            isprime= False
            break
    if isprime:
        p = n
        i=1
        while isprime and i<len(str(n)):

            l = p % 10
            k = p // 10
            p = int(str(l) + str(k))
            #print(n,p)
            for j in range(2,int(p**0.5)+1):
                if p % j == 0:
                    isprime = False
                    break
            i+=1
    if isprime:
        count+=1
        print("count",count,n)

    n+=1