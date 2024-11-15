import random
import os

list=[]
n=1000

for i in range(n):
    list.append(random.randint(0,100))

smal = min(list)
maxi = max(list)

scount = list.count(smal)
mcount = list.count(maxi)


os.system("cls")
print("Suurin luku on", maxi, "ja se on", mcount, "kertaa listassa")
print("Pienin luku on", smal, "ja se on", scount, "kertaa listassa")