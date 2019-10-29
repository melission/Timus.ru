import sys

device = []
price = []
inpcount = 0
var = 1
for line in sys.stdin:
    # print('var: ', var)
    line = line.strip()
    if inpcount % 3 == 0 or inpcount == 0:
        line = line
    elif var == 2:
        price.append(line)
        var = 1
    elif var == 1:
        device.append(line)
        var = 2
    inpcount += 1
# print(device)
# print(price)
#
#
# d = {}
mostpopular = {}

count = 0
for item in device:
    if item in mostpopular:
        mostpopular[item] += 1
    if item not in mostpopular:
        mostpopular[item] = 1

pop = ''
val = 0

for value in mostpopular.items():
    print(value)
    if val < value[1]:
        pop = value[0]
        val = value[1]
        print('loop: ', pop, val)
print(pop, val)
minprice = {}






# print(d)
# print(mostpopular)
# print(pop)
