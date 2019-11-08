# ru: https://habr.com/ru/post/455722/
# eng: https://habr.com/ru/post/458518/
import sys

itemcount = int(input().strip())
toSortList = []

for i in range(itemcount):
    str_lst = input().strip().split()
    # print(len(str_lst))
    str_lst[1] = int(str_lst[1])
    # team = []
    # for srt_num in str_lst:
    #     num = int(srt_num)
    #     team.append(num)
    toSortList.append(str_lst)
print(sys.getsizeof(toSortList))


# print(toSortList)
# print(type(toSortList[0][0]))

def bubble_sort(toSortList):
    changed = True
    r = range(len(toSortList) - 1)
    while changed:
        changed = False
        for item in r:
            if toSortList[item][1] < toSortList[item+1][1]:
                toSortList[item], toSortList[item+1] = toSortList[item+1], toSortList[item]
                changed = True
    return toSortList


# print(bubble_sort(toSortList))
sortedList = bubble_sort(toSortList)
for item in sortedList:
    print('{} {}'.format(item[0], item[1]))


