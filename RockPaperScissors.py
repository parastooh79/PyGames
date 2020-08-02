from random import randint
CoputerPoint = 0
UserPoint = 0
for  i in range(10):
    inp = input('ENTER Rock Paper Scissors :')
    if inp == "R" or inp == "r":
        inp = 1
    if inp == "P" or inp == "p":
        inp = 2
    if inp == "K" or inp == "k":
        inp = 3
    ran = randint(1, 3)
    if ran == 1 and inp == 2 or ran == 2 and inp == 3 or ran == 3 and inp == 1:
        UserPoint += 1
        print("USER WIIIN")
    if ran == 1 and inp == 3 or ran == 2 and inp == 1 or ran == 3 and inp == 2:
        CoputerPoint += 1
        print("COMPUTER WIIIN")
    if ran == 1 and inp == 1 or ran == 2 and inp == 2 or ran == 3 and inp == 3:
        print("NO ONE WIN")
print("COMPUTER POINT :"+str(CoputerPoint)+" | "+"USER POINT :"+str(UserPoint))
