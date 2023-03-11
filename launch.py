# progs
import main as m

listOfProgs = ['main']
curNum = 0

print("WELLCOME TO ISH_SOFT!")
print("CHOOSE NEEDED SOFT:")

for items in listOfProgs:
    print(f"[{curNum}] | {listOfProgs[curNum]}")
    curNum += 1

run = input("ENTER SOFT NUM: ")

if run == "0":
    m.main_soft()
else:
    print("INVALID NAME!")
