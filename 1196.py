# http://acm.timus.ru/problem.aspx?space=1&num=1196&locale=en

teachdates = int(input().strip())
teacherslist, studentslist = [], []
for i in range(teachdates):
    inpdate = input()
    teacherslist.append(inpdate.strip())
studentinput = int(input())
for i in range(studentinput):
    inpdate = input()
    studentslist.append(inpdate.strip())

# print(teacherslist, studentslist)
match = 0
for item in studentslist:
    if item in teacherslist:
        match += 1

print(match)