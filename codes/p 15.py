sum1=1
i=20
m=1

for j in range(1,i+1,1):
    n=0

    for k in range(1,j+1,1):

        while True:
            x=0
            p=1
            for l in range(1,j+1,1):
                p*=l
            q = 1
            if j == k:
                q = 1
            else:
                for l in range(1, j - k + 1,1):
                    q *= l
            r = 1
            for l in range(1, k + 1,1):
                r *= l
            x=p/(q*r)
            sum1+=x
            n+=x
            print(j,x)
            break
    print("asfhghj",j,n)
    m+=n
#print("ggh",j)

for j in range(j-1,0,-1):
    v=j
    n=0

    for k in range(1, v + 1,1):

        while True:
            x = 0
            p=1
            for l in range(1,v+1,1):
                p*=l
            q = 1
            if j == k:
                q = 1
            else:
                for l in range(1, v - k + 1,1):
                    q *= l
            r = 1
            for l in range(1, k + 1,1):
                r *= l
            x=p/(q*r)
            sum1+=x
            n+=x
            print(v, x)
            break
    print("asfhghj",v, n)
    m+=n


print(sum1)
print(m)