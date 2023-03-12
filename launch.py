# colorama stuff
from colorama import init, Fore, Back, Style
init()

listOfProgs = ['load-toy', 'msg-write', 'love-bot']
curNum = 0

print(Fore.BLUE + "WELLCOME TO ISH_SOFT!")
print(Fore.BLUE + "CHOOSE NEEDED SOFT:")

for items in listOfProgs:
    print(Fore.BLUE + f"[{curNum}] | {listOfProgs[curNum]}")
    curNum += 1


run = input(Fore.BLUE + "ENTER SOFT NUM: ")

if run == "0":
    print(" \n ")
    import load
    load

elif run == "1":
    print(" \n ")
    import henlo
    henlo

elif run == "2":
    print(" \n ")
    import loveBot
    loveBot

else:
    print(Fore.BLUE + "INVALID NAME!")
