mydict={}
count=0
for i in range(10,100):
    
    p=[l for l in str(i)]
    p=list(map(int,p))
    k=p
    if p[0]==p[1]:
        continue
    
    for j in range(99,i,-1):
        #print(i,j)
        
            
        p=[l for l in str(i)]
        p=list(map(int,p))
        

        q=[l for l in str(j)]
        q=list(map(int,q))
        
        #print(i,p,q,j)

    
        if q[0]==q[1]:
            continue
        
        intersection=list(set(p) & set(q))
        
        if intersection==[] or intersection[0]==0:
            continue
        #print("KKK",i,j,intersection[0])
        p.remove(intersection[0])
        q.remove(intersection[0])
        if q[0]==0:
            continue
        if (i/j)==(p[0]/q[0]):
            mydict[i]=j
            count+=1
        #p.clear()
        #q.clear()
print(mydict)
numerator=1
denominator=1
for i in mydict:
    numerator*=i
    denominator*=mydict[i]
print(numerator,denominator,denominator/numerator)
    
        
        
