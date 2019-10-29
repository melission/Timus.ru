# http://acm.timus.ru/problem.aspx?space=1&num=1893&locale=en


seat = input().strip()
seatnum = seat[:-1]
seatnum = int(seatnum)
seatletter = seat[-1].capitalize()
# print(type(seatletter))
if seatnum <= 2:
    if seatletter == 'A' or seatletter == 'D':
        print('window')
    else:
        print('aisle')

if 2 < seatnum <= 20:
    if seatletter == 'A' or seatletter == 'F':
        print('window')
    else:
        print('aisle')

if 20 < seatnum <= 65:
    if seatletter == 'A' or seatletter == 'K':
        print('window')
    elif seatletter == 'C' or seatletter == 'D' or seatletter == 'G' or seatletter == 'H':
        print('aisle')
    else:
        print('neither')