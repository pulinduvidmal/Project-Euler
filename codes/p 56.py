maxvalue=0
for a in range(1,100):
    for b in range (1,100):
        sumvalue=0
        for i in str(a**b):
            sumvalue+=int(i)
        if sumvalue>maxvalue:
            maxvalue=sumvalue
print(maxvalue)
        
        
        
