# http://acm.timus.ru/problem.aspx?space=1&num=1263&locale=en

import sys

n_politicians, n_people = input().split()
n_politicians = int(n_politicians)
votes = {}

for politicians in range(1, n_politicians+1):
    votes[politicians] = 0

for line in sys.stdin:
    line = int(line.strip())
    if line not in votes:
        votes[line] = 0
    if line in votes:
        votes[line] += 1
# print(votes)
for result in votes:
    percentage = int(votes[result])*100/int(n_people)
    print('{}{}'.format('%.2f' % percentage, '%'))




