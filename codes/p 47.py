def f(y):
    if y==2:
        return True
    if y%2==0:
        return False
    
    for i in range (3,int(y**0.5)+1,2):
        if y%i==0:
            return False
    else:
        return True
print(f(491))

def g(x):
    list1=[]
    
    while x%2==0:
        x=x//2
        list1.append(2)
    #
    #print(n,x)
    
    for i in range(3,int(x**0.5)+1,2):
        while x%i==0:
            
            list1.append(i)
            x=x//i

    if x>1:
        list1.append(x)
    return list1
    

n=12
while True:
    list1=[]
    #
    #print(n,g(n))
    if len(set(g(n)))==len(set(g(n+1)))==len(set(g(n+2)))==len(set(g(n+3)))==4 :
        print(n)
        break
    n+=1
    #if n==20:
      #  break
   
