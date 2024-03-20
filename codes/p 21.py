i=1
suma=0
while i<10000:
        sum1=1
        for j in range(2,i//2+2):
            if i%j==0:

                sum1+=j
        sum2=1
        for k in range(2,sum1//2+2):
            if sum1%k==0:
                sum2+=k
        if i==sum2:
            if i!=sum1:
                print(i, sum1)
                suma=suma+i+sum1


        i+=1
print(suma/2)