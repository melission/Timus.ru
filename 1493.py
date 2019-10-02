# http://acm.timus.ru/problem.aspx?space=1&num=1493&locale=en
import sys
frst_half = []
scnd_half = []
next_ticket_num = 0
for str_num in sys.stdin:
    next_ticket_num = str_num[3:].strip()
    for item in str_num[:3].strip():
        item = int(item)
        frst_half.append(item)
    for item in str_num[3:].strip():
        item = int(item)
        scnd_half.append(item)

