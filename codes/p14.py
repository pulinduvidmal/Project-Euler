units =int(input("number of units"))
x = int(input("number of days"))
kwhcharge=0
fixedcharge=0
total=0
if (units<2*x) :
    if (units<=x) :
        kwhcharge = x*2.50
        fixedcharge = 30
    else:
        kwhcharge = x*2.50 +(units-x)*4.50
        fixedcharge = 60
elif(units<=3*x):
    kwhcharge = (2*x)*7.85 +(units-(2*x))*10
    fixedcharge =90
    
elif(units<=4*x):
    kwhcharge = (2*x)*7.85 +x*10 +(units-(3*x))*27.75
    fixedcharge = 480
    
elif(units<=6*x):
    kwhcharge = (2*x)*7.85 +x*10 + x*27.75 +(units-(4*x))*32
    fixedcharge = 480

else :
    kwhcharge = (2*x)*7.85 +x*10 + x*27.75 +(2*x)*32+(units-(6*x))*45
    fixedcharge = 540
    
total=(kwhcharge +fixedcharge)
print(total)
