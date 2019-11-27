# https://acm.timus.ru/problem.aspx?space=1&num=1935


def bubble_sort(numList):
    changed = True
    while changed:
        changed = False
        for i in range((len(numList)-1)):
            if numList[i] > numList[i+1]:
                numList[i], numList[i+1] = numList[i+1], numList[i]
                changed = True
    return numList


ingredients = int(input())
distanceBetween = input().split()
for item in range(0, len(distanceBetween)):
    distanceBetween[item] = int(distanceBetween[item])
sortedDistanceBetween = bubble_sort(distanceBetween)
totalLists = distanceBetween[0]
for dist in range(ingredients-1):
    # print(dist)
    if distanceBetween[dist] < distanceBetween[dist+1]:
        totalLists = totalLists + distanceBetween[dist+1]
        # print('if: ', totalLists)
    else:
        totalLists = totalLists + distanceBetween[dist]
        # print('else: ', totalLists)
totalLists = totalLists + distanceBetween[-1]
print(totalLists)

