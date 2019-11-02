team_ZZZ, team_QXX = input().strip().split()

bedug = input().strip().split()
sum_debug = 0
for item in bedug:
    sum_debug = sum_debug + int(item)
debugtimeinminuts = 20
if sum_debug*debugtimeinminuts+int(team_ZZZ) > int(team_QXX):
    print('Dirty debug :(')
if sum_debug*debugtimeinminuts+int(team_ZZZ) < int(team_QXX):
    print('No chance.')
if sum_debug*debugtimeinminuts+int(team_ZZZ) == int(team_QXX):
    print('No chance.')
