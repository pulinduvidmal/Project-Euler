list1=[]
for i in range(100,1000):
    for j in range(100,1000):

        v=i*j
        x=""
        for l in (str(v)):
            x=str(l)+x
            if v==(int(x)):
                print(i,"  ",j,"  ",v)
                list1.append(v)
print(max(list1))

