from random import randint
CoputerPoint = 0
UserPoint = 0
for  i in range(10):
    inp = input('ENTER S K G :')
    if inp == "S" or inp == "s":
        inp = 1
    if inp == "K" or inp == "k":
        inp = 2
    if inp == "G" or inp == "g":
        inp = 3
    ran = randint(1, 3)
    if ran == 1 and inp == 2 or ran == 2 and inp == 3 or ran == 3 and inp == 1:
        UserPoint += 1
        print("User WIIIN")
    if ran == 1 and inp == 3 or ran == 2 and inp == 1 or ran == 3 and inp == 2:
        CoputerPoint += 1
        print("Computer WIIIN")
    if ran == 1 and inp == 1 or ran == 2 and inp == 2 or ran == 3 and inp == 3:
        print("NO ONE WIIIN")
print("COMPUTER POINT :"+str(CoputerPoint)+" | "+"USER POINT :"+str(UserPoint))
