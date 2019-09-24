# http://acm.timus.ru/problem.aspx?space=1&num=2056&locale=en

import  sys
exam_count = int(input())
assessment = []
for item in sys.stdin:
    if int(item) == 3:
        print('None')
        quit()
    assessment.append(int(item))

if sum(assessment) // 5 == exam_count:
    print('Named')
elif sum(assessment) / len(assessment) >= 4.5:
    print('High')
else:
    print('Common')
