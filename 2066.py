frst = int(input())
scnd = int(input())
thrd = int(input())
# min_value = min(frst-scnd-thrd, frst-scnd*thrd)
# print(min_value)

if scnd != 0:
    min_value = - thrd * scnd + frst
else:
    min_value = - thrd + scnd * frst

print(min_value)