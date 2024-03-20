list1=[]
x=open('C:\\Users\\Pulindu\\Desktop\\p022_names.txt','r')
for i in x:
    list1=i.split(",")
list1.sort()
#print(list1)
#print(list1.index('"COLIN"')+1)
x='"ABCDEFGHIJKLMNOPQRSTUVWXYZ'
list2=[]
list3=[]
for i in x:
    list2.append(i)
for i in (list2):
    print(i,list2.index(i))
for k in range(1,27):
    list3.append(str(k))



sum2=0
for i in list1:
    
    print(i)
    sum1=0
    for x in i:
        k=list2.index(x)
        sum1+=k
    p=(list1.index(i)+1)*sum1
    sum2+=p
print(sum2)
    
  

        
            


    
