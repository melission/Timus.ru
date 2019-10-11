# http://acm.timus.ru/problem.aspx?space=1&num=1493&locale=en
import sys
frst_half = []
scnd_half = []
frst_part = 0
scnd_part = 0
for str_num in sys.stdin:
    frst_part = str_num[3:].strip()
    scnd_part = str_num[3:].strip()
    for item in str_num[:3].strip():
        item = int(item)
        frst_half.append(item)
    for item in str_num[3:].strip():
        item = int(item)
        scnd_half.append(item)

