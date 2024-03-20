
from itertools import permutations
p=permutations('1234567890')
list_prime=[2,3,5,7,11,13,17]
sum_num=0
for i in list(p):
    str_num=""
    #print(i)
    for j in i:
        str_num+=j
    for i in range(7):
        num=str_num[i+1]+str_num[i+2]+str_num[i+3]
        if int(num)%(list_prime[i])!=0:
            break
    else:

        
        sum_num+=int(str_num)
    #print(str_num)   
print(sum_num)

