
import sys

imp = []
for line in sys.stdin:
    for item in line.split():
        imp.append(int(item.strip()))
agreement = 0
while True:
    agreement = agreement + (imp[0] + imp[1])

