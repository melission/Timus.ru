tottasks = 12
scndfivehour = (60*4) // 45
#how much tasks he needs to solve at frst hour
frsthour = int(input())
if frsthour >= tottasks-scndfivehour:
    print('YES')
else:
    print('NO')