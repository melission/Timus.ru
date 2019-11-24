# https://acm.timus.ru/problem.aspx?space=1&num=1617

wheelNum = int(input())
typeWheel = {}
for i in range(wheelNum):
    wheel = input().strip()
    if wheel in typeWheel:
        typeWheel[wheel] += 1
    if wheel not in typeWheel:
        typeWheel[wheel] = 1

# print(typeWheel)
equippedWagon = 0
for wheel in typeWheel.values():
    equippedWagon = equippedWagon + wheel//4

print(equippedWagon)

