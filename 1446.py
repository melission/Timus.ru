import sys

inputNum = int(input())
Slytherin, Gryffindor, Hufflepuff, Ravenclaw = [], [], [], []

for i in range(inputNum):
    name = input().strip()
    houseName = input().strip()
    # print('name: ', name, 'house: ', houseName)
    if houseName == 'Slytherin':
        Slytherin.append(name)
    if houseName == 'Gryffindor':
        Gryffindor.append(name)
    if houseName == 'Hufflepuff':
        Hufflepuff.append(name)
    if houseName == 'Ravenclaw':
        Ravenclaw.append(name)

print('Slytherin:')
for name in Slytherin:
    print(name)

print('\nHufflepuff:')
for name in Hufflepuff:
    print(name)

print('\nGryffindor:')
for name in Gryffindor:
    print(name)

print('\nRavenclaw:')
for name in Ravenclaw:
    print(name)
print('\n')
