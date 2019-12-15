J = "aA"
S = "aAAbbbb"
jList = J.split()
sList = S.split()
jewCount = 0
for jewel in jList:
    print(jewel)
    for stone in sList:
        print(stone)
        if jewel == stone:
            jewCount += 1


