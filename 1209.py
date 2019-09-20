import sys
import time

count_of_call = int(input())
# add variable to assume this to the power og numbers
str_power = ''
# import all position numbers and add them to the list 'position'
position = []
for line in sys.stdin:
    position.append(int(line))
# solution of this task has to be less than one second
start_time = time.time()
# assume maximum number of 'position' list to the variable 'pow_num'
pow_num = int(max(position)) + 1
# print('max of position: ', pow_num)
for power in range(0, pow_num):
    if len(str_power) >= pow_num:
        break
    # print('power in range: ', power)
    str_power = str_power + str(10 ** power)

# print('str_power: ', str_power)

output_position = []
for char in position:
    # print('len of powernum: ', len(str_power))
    # print('char: ', char)
    if len(str_power) >= int(char):
        output_position.append(str_power[int(char) - 1])
# print('out list: ', output_position)
# constitute all numbers into one string
outpur_str = ' '.join(output_position)
print(outpur_str)

print("--- %s seconds ---" % (time.time() - start_time))
