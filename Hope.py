#EXPORT
#2
#4
#Hope
c = 0
for i in range(1,250):
    if i % 2 == 0:
        if c < 2 :
            print(i)
            c += 1
        if c==2:
            print('Hope')
            c = 0
