# http://acm.timus.ru/problem.aspx?space=1&num=1585&locale=en

import sys

lines = int(input())
names = {}
for name in sys.stdin:
    cleaned_name = name.strip()
    if cleaned_name not in names:
        names[cleaned_name] = 0
    if cleaned_name in names:
        names[cleaned_name] += 1

lst_names = list(names.items())
lst_names.sort(key=lambda val: val[1])
print(lst_names[-1][0])
