# http://acm.timus.ru/problem.aspx?space=1&num=2056&locale=en
from statistics import median_grouped
import  sys
exam_count = int(input())
assessment = []
for item in sys.stdin:
    assessment.append(int(item))

mid = median_grouped(assessment)

if 3 in assessment:
    print('None')
elif mid == 5:
    print('Named')
elif mid >= 4.5:
    print('High')
else:
    print('Common')
