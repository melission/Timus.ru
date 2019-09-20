lock1 = int(input())
lock2 = int(input())
keys = {lock1: lock2, lock2: lock1}
stealkey = 0
curlock = lock1
while stealkey <= 9999:
    if stealkey == curlock:
        print('yes')
        break
    stealkey = stealkey + 1
    curlock = keys[curlock]
    if stealkey == 9999:
        print('no')
