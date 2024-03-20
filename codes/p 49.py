for x in range(1000,6670):

    isprime=True
    for i in range(2,x):
            if x%i==0:
                isprime=False
                break

    if isprime:
        y=x+3330
        isprime = True
        for i in range(2, x):
                if x % i == 0:
                    isprime = False
                    break

        if isprime:
            z=y+3330
            isprime = True
            for i in range(2, x):
                    if x % i == 0:
                        isprime = False
                        break

            if isprime:
                if True:
                    #print("hiiiiiiii",x,"  ",y,"  ",z)
                    list1=[]
                    for a in (str(x)):

                        list1.append(a)
                    list1.sort()
                    #print(list1)
                    list2 = []
                    for b in (str(x)):
                        list2.append(b)
                    list2.sort()
                    #print(list2)
                    list3=[]
                    for c in (str(z)):
                        list3.append(c)
                    list3.sort()

                    if list1==list2==list3:
                        print(x,"  ",y,"  ",z)