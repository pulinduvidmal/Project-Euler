dict_letter={}
n=1
for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    dict_letter[i]=n
    n+=1

text=open("C:\\Users\\ULTIMO\\Downloads\\p042_words.txt",'r')
p=text.read()
list_letter=p.strip().split(",")

#print(list_triangle)
import math
count=0
for i in list_letter:
    sum_letter=0
    for j in i[1:-1]:
        sum_letter+=dict_letter[j]

    squrt_num=math.sqrt(4*2*sum_letter+1)
    if squrt_num%1==0.0:
        count+=1
      
print(count)   
