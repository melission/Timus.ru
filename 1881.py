# http://acm.timus.ru/problem.aspx?space=1&num=1881&locale=en

import sys

listline, chars, woldsnum = input().split()
inputwords = []
for line in sys.stdin:
    inputwords.append(line.strip())
fillin = int(chars)
line = int(listline)
# print('fillin: ', fillin)
numpages = 1
for word in inputwords:
    if len(word) <= fillin:
        fillin = fillin - len(word)
        if fillin < 0:
            line -= 1
            fillin = int(chars) - len(word)
            if line == 0:
                line = int(listline)
                numpages += 1
        # print(word, fillin)
    elif len(word) >= fillin:
        line -= 1
        if line == 0:
            line = int(listline)
            numpages += 1
        fillin = int(chars) - (len(word))

    if fillin > 0:
        fillin -= 1

        # print(word, fillin)
# print(line)
print(numpages)


