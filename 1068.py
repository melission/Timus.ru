number = int(input())
sum = 0
if number > 0:
    for num in range(1, number+1):
        # print(num)
        sum = sum + num
        # print(sum)
if number < 1:
    for num in range(number, 2):
        # print(num)
        sum = sum + num
        # print(sum)

print(sum)