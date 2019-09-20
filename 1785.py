count = int(input())
if count > 0 and count < 5:
    print('few')
if count > 4 and count < 10:
    print('several')
if count > 9 and count < 20:
    print('pack')
if count > 19 and count < 50:
    print('lots')
if count > 49 and count < 100:
    print('horde')
if count > 99 and count < 250:
    print('throng')
if count > 249 and count < 500:
    print('swarm')
if count > 499 and count < 1000:
    print('zounds')
if count > 999:
    print('legion')