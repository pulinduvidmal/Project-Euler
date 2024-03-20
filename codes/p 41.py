def f(x):
    
    for j in range(2,int(x**0.5)+1):
        if x%j==0:
            return 0
        
    else:
        return 1
        
str_largest_Pandigital_number="987654321"

import itertools

not_find=True
while not_find:
    
    permutations_list=[int(''.join(p)) for p in itertools.permutations(str_largest_Pandigital_number)]
    for i in permutations_list:
        if str(i)[len(n)-1]=="1" or str(i)[len(n)-1]=="3" or str(i)[len(n)-1]=="7" or str(i)[len(n)-1]=="9":
            
            if f(i)==1 :
                
                print(i)
                not_find=False
                break
                
            
            
        
    str_largest_Pandigital_number=str_largest_Pandigital_number[1:]
    
            
        
    
    
                                                     

