from math import sqrt
import sys

# nums = input()
# print(nums)
num_lst = []

for line in sys.stdin:
    for item in line.split():
        num_lst.append(item)
out_lst = []
for item in num_lst:
    root = sqrt(float(item))
    root = float('{:.4f}'.format(root))
    out_lst.append(root)
out_lst.reverse()
for num in out_lst:
    print("{:0.4f}".format(num))
