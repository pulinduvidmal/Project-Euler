list1=",one,two,three,four,five,six,seven,eight,nine".split(",")
list1=list(map(str,list1))
list2="ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen".split(",")
list2=list(map(str,list2))
list3="twenty,thirty,forty,fifty,sixty,seventy,eighty,ninety".split(",")
list3=list(map(str,list3))
list4=["","hundred"]
list5=["","And"]
list6=["onethousand"]
list7=["","-"]

i=0
r=0
f=0
sum1=0
flag=True
while flag:
    for j in range(10):
        if i%100==0:
            f=0
        sum1 += len(list1[int(i / 100)] + list4[r] + list5[f] + list1[j])
        print(i,list1[int(i/100)],list4[r],list5[f],list1[j],len(list1[int(i/100)]+list4[r]+list5[f]+list1[j]),sum1)

        i += 1
        if i>100:
            f=1

    for j in range(10):
        sum1 += len(list1[i // 100] + list4[r] + list5[f] + list2[j])
        print(i,list1[i//100],list4[r],list5[f],list2[j],len(list1[i//100]+list4[r]+list5[f]+list2[j]),sum1)

        i += 1
    for j in range(20,100):
        sum1 += len(list1[i // 100] + list4[r] + list5[f] + list3[((i % 100) // 10) - 2] + list1[j % 10])
        print(i,list1[i//100],list4[r],list5[f],list3[((i%100)//10)-2],list1[j%10],len(list1[i//100]+list4[r]+list5[f]+list3[((i%100)//10)-2]+list1[j%10]),sum1)

        i += 1
        if i == 999:
            flag = False
    r=1
    f=1


print(sum1+len(list6[0]))