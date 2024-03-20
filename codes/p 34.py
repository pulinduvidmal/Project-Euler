
for j in range(3,362880):
    sum1=0
    for k in (str(j)):
        h=1
        for l in range(1,int(k)+1):
            h=h*l
        sum1+=h
    if j==sum1:
        print(j)