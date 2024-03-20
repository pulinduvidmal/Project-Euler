def f(n):
    return n*(n+1)/2

def g(n):
    return n*(3*n-1)/2

def d(n):
    return n*(2*n-1)
list1=[]
list2=[]
list3=[]
for i in range(1,100000):
    list1.append(f(i))
    list2.append(g(i))
    list3.append(d(i))
set1=set(list1)
set2=set(list2)
set3=set(list3)

print(set1&set2&set3)
