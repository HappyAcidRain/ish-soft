
listOfProgs = ['load-toy', 'msg-write', 'love-bot']
curNum = 0

print("WELLCOME TO ISH_SOFT!")
print("CHOOSE NEEDED SOFT:")

for items in listOfProgs:
    print(f"[{curNum}] | {listOfProgs[curNum]}")
    curNum += 1

run = input("ENTER SOFT NUM: ")

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
    print("INVALID NAME!")
