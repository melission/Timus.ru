import sys
# assume next variable to the value of guests
num_guests = int(input())
# lets import all invitations and add them to the list. wa can do this split every line out if this line contains '+'.
# if line doesnt contains '+' then we just add this line to the list of names
names = []
for line in sys.stdin:
    if '+' in line:
        for item in line.split('+'):
            names.append(item)
    else:
        names.append(line)
# we also have 2 guests on this wedding: this is married couple. add them to the total number of guests
totnumguests = len(names) + 2
if totnumguests == 13:
    totnumguests = totnumguests + 1

cost = totnumguests * 100
print(cost)