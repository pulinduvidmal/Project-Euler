list1=[]
for i in range(2,101):
    for j in range(2,101):
        list1.append(i**j)

list2=[]
for k in list1:
    if k not in list2:
        list2.append(k)
print(list2)
print(len(list2))