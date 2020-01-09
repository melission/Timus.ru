registredUsers = {}


def register(username, password):
    if username not in registredUsers.keys():
        registredUsers[username] = [password, {'status': False}]
        return 'success: new user added'
    else:
        return 'fail: user already exists'


def login(username, password):
    if username not in registredUsers.keys():
        return print('fail: no such user')
    if registredUsers[username][0] != password:
        return print('fail: incorrect password')
    if registredUsers[username][1]['status'] == True:
        return print('fail: already logged in')
    if registredUsers[username][1]['status'] == False:
        registredUsers[username][1]['status'] = True
        return print('success: user logged in')


def logout(username):
    if username not in registredUsers.keys():
        return print('fail: no such user')
    if not registredUsers[username][1]['status']:
        return print('fail: already logged out')
    if registredUsers[username][1]['status']:
        registredUsers[username][1]['status'] = False
        return print('success: user logged out')


inputLines = int(input())
for lines in range(inputLines):
    info = input().strip().split()
    if info[0] == 'register':
        # print(info)
        print(register(username=info[1], password=info[2]))
    if info[0] == 'login':
        # print(info)
        login(username=info[1], password=info[2])
    if info[0] == 'logout':
        # print(info)
        logout(username=info[1])
    # print(registredUsers)
