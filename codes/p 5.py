r=1
for l in range(2,21):
    r*=l




for i in range(2, 21):
    if r % i ==0:
        true=True
        while true:
            for j in range(2, 21):
                if (r // i) % j != 0:
                    true = False
                    break
            if true:
                r = r // i
print(r)

