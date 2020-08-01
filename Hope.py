c = 0
inp = int(input("Enter range number : "))
EvenOdd = input("Even or Odd ? (use E = e or D = d) : ")
HopeJump=int(input('Enter Hope Jump number :'))
for i in range(1,inp):
    if EvenOdd == 'E' or EvenOdd == 'e':
        if i % 2 == 0:
            if c < HopeJump:
                print(i)
                c += 1
            if c == HopeJump:
                print('Hope')
                c = 0
    if EvenOdd == 'D' or EvenOdd == 'd':
        if i % 2 == 1:
            if c < HopeJump:
                print(i)
                c += 1
            if c == HopeJump:
                print('Hope')
                c = 0
