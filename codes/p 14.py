list2 = []
n=1
i=1
while i<1000000:
    list1=[n]
    while True:
        if n==1:
            break
        if n%2 == 0:
            n=n//2
        else:
            n=3*n+1
        list1.append(n)

    if len(list2) < len(list1):
        list2 = list1
        print("kk", list2)

    i+=2
    n=i
print(list2)