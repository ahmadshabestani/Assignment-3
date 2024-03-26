import random
import sys

tedad = int(input("tedad arraye ra vared konid :"))
n = []
for i in range(0, tedad):
    randoms = random.randint(0, sys.maxsize)
    if randoms in n:
        continue
    else:
        n.append(randoms)
    print(n)
