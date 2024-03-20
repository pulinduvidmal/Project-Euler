listnum=[1,2,3,4,5,6,7,8,9]

n=1

list_product=[]
while n<3:
    for a in range(10**(n-1),10**n):
        
        for b in range(10**(4-n),10**(5-n)):
            #print(j)
            list1=[]
            
            if b==189:
                if a==39:
                    
                    
                    print("hi")
            p=str(a)+str(b)+str(a*b)
            if len(p)==9:
                for l in p:
                    list1.append(int(l))
                #list1=list(map(int,list1))
                #print(set(list1))
                list1.sort()
                if list1==listnum:
                    list_product.append(a*b)
                    
            

    n+=1                    
#list>>>set 
print(sum(set(list_product)))
                
