import time
number = int(input())
start_time = time.time()
summ = 0
if number > 0:
    summ = sum(range(1, number+1))
if number < 1:
    summ = sum(range(number, 2))

print(summ)
print("--- %s seconds ---" % (time.time() - start_time))