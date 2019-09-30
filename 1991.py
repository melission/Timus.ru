# http://acm.timus.ru/problem.aspx?space=1&num=1991&locale=en

blocks, droids = input().split()
blocks, droids = int(blocks), int(droids)
tot_explosion = input().split()
survived_droids = 0
untouched_explosion = 0

for block in tot_explosion:
    calc = droids - int(block)
    if calc > 0:
        survived_droids += calc
    if calc < 0:
        untouched_explosion += abs(calc)

print('{} {}'.format(untouched_explosion, survived_droids))

