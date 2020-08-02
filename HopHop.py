Counter = 0
Hope = 5 #input("What Your Hope Point : ")
for i in range(1000):
    i = i+1
    if i%5==0:
        I = input("Enter Your Number : ")
        if I == "H":
            print("True")
        else:
            print(">>> U LOSE THIS GAME SAY HOPE <<<")
            break
    else:
        I = int(input("Enter Your Number : "))
        if I == i:
            print("True")
        else:
            print(">>> U LOSE THIS GAME SAY TRUE NUMBER <<<")
