import os
print('--------------> JimByte Make it <--------------')
print("GAMES : ")
print(os.system("ls data"))
print('-----------------------------------------------')
inp=input("choos the game File : ")
response = os.system("python3 " + inp)
