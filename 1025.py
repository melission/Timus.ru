# http://acm.timus.ru/problem.aspx?space=1&num=1025&locale=en
import math
crowds = int(input())
population = input().split()
population = list(map(lambda num: int(num), population))
population = sorted(population)
# print('population: ', population)
majority = math.ceil((crowds + 1) / 2)
# print('maj: ', majority)
democracybite = 0
for digit in range(majority):
    # print('number of crowd: {}, population of crowd: {}, total of loyal: {}'.format(digit, population[digit], democracybite))
    democracybite = democracybite + int(population[digit]) / 2
    democracybite = math.ceil(democracybite)

print(democracybite)
