import math
meal, caparacity = input().split()
meal, caparacity = int(meal), int(caparacity)
peroneside = 0
for frst in range(1):
    peroneside = meal - caparacity
    if peroneside < 0:
        peroneside = 1

for item in range(1, meal):
    if meal - caparacity < 0:
        peroneside = peroneside + 1
        break
    if meal - caparacity > 0:
        peroneside = peroneside + 1

print(peroneside)


