# http://acm.timus.ru/problem.aspx?space=1&num=1563&locale=en

import sys
total_shops = int(input())
visited_shop = []
duplicates = 0

for name in sys.stdin:
    if name in visited_shop:
        duplicates += 1
    if name not in visited_shop:
        visited_shop.append(name)

print(duplicates)
