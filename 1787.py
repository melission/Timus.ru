import math
carperminute, minutes = input().split()
incomecars = input().split()
traffic = 0
for car in incomecars:
    traffic = traffic + (int(car) - int(carperminute))
    if traffic < 0:
        traffic = 0

print(traffic)