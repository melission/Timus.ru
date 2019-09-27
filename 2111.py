# http://acm.timus.ru/problem.aspx?space=1&num=2111&locale=en

import sys
tot_cities = int(input())

roads = []
for road in sys.stdin:
    for r in road.split():
        roads.append(r)
# print('roads: ', roads)

baggage = 0

for item in roads:
    baggage = baggage + int(item)
# print('bagg: ', baggage)

taxes = 0

for trip in roads:
    taxes = taxes + (baggage*int(trip))
    # print('t1:', taxes)
    baggage = baggage - int(trip)
    # print(baggage)
    taxes = taxes + (baggage*int(trip))
    # print('t2: ', taxes)

print(taxes)
