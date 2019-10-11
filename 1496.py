# http://acm.timus.ru/problem.aspx?space=1&num=1496&locale=en
import sys


num_line = int(input())
names = {}
for name in sys.stdin:
    name = name.strip()
    if name in names:
        names[name] += 1
    if name not in names:
        names[name] = 1

for nm in names.items():
    val = nm[1]
    key = nm[0]
    # print('key, val: ', key, val)
    if val > 1:
        print(key)
