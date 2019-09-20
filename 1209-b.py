import sys
import time

count_of_call = int(input())
# add variable to assume this to the power og numbers
str_power = ''
# import all position numbers and add them to the list 'position'
position = []
for line in sys.stdin:
    position.append(int(line))

# max_position = max(position)
# if max_position > (2**31)-1:
#     max_position = (2**31)-1
# print('msx position: ', max_position)

# create a new list and add all position of number '1' to this list
pos_one = []
number = 0
for one in range(0, 32):
    number = number + one
    pos_one.append(number)
print('position one: ', pos_one)
# now i have every position number of '1', and i can compare every integer from list 'position' with integer of '1' from
# list 'pos_one'. if integer from 'position' not in 'pos_one', then this integer is '0', if this integer in 'pos_one',
# than this integer is '1'
# create new list and add all numbers from for-loop than contains if integer in 'pos_one' or not
out_lst = []
for item in position:
    # print('item in position: ', item)
    if (item-1) in pos_one:
        out_lst.append(str(1))
    if (item-1) not in pos_one:
        out_lst.append(str(0))
# constitute all numbers from our_lst to the string with '.join' and print this.
output_str = ' '.join(out_lst)

print(output_str)
