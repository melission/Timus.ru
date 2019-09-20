import sys
nums = []
for line in sys.stdin:
    nums.append(line)

a1, b1 = nums[0].split()
a2, b2 = nums[1].split()
a3, b3 = nums[2].split()
frstberry = int(a1) - int(a3)
scndberry = int(b1) - int(b2)

print(frstberry, scndberry)