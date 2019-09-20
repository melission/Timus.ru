import sys

num_letters = int(input())
names = []
# add every name on the letter into one dictionary
for name in sys.stdin:
    names.append(name[0])

letters = ['A, P, O, R', 'B, M, S', 'D, G, J, K, T, W']

position = 0
steps = 0
for name in names:
    for item in letters:
        if name in item:
            variable = letters.index(item)
            # print(letters.index(item))
            if position == variable:
                steps = steps
            if position < variable:
                steps = steps + (variable - position)
                position = variable
            if position > variable:
                steps = steps + (position - variable)
                position = variable

print(steps)







