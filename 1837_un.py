
numberofteam = int(input().strip())
engineers = {'Isenbaev': 0}
name = 'Isenbaev'
for i in range(numberofteam):
    team = input().strip().split()
    if name in team:
        for item in team:
            # print(team)
            if item != name:
                # print(item)
                engineers[item] = 1
    if name not in team:
        for item in team:
            if item not in engineers:
                print(item)


print(engineers)

