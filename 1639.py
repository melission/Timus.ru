a, b = input().split()
a, b = int(a), int(b)
if (a * b) % 2 == 0:
    print('[:=[first]')
if (a * b) % 2 == 1:
    print('[second]=:]')
