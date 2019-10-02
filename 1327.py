# http://acm.timus.ru/problem.aspx?space=1&num=1327&locale=en
import math

first_day = int(input())
last_day = int(input())

# if first_day % 2 == 0:
#     first_day += 1
if first_day % 2 == 1:
    first_day -= 1

tot = (last_day - first_day)/2

tot = math.ceil(tot)
print(tot)
