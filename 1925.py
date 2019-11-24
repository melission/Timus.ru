

totalYear, currentYear = input().split()
totalYear, currentYear = int(totalYear), int(currentYear)
alienNum, humanNum = [], []
for i in range(totalYear):
    alien, human = input().split()
    alienNum.append(int(alien)), humanNum.append(int(human))
# print(alienNum, humanNum)
totalAlienNum = sum(alienNum) + currentYear
totalHumanNum = sum(humanNum) + len(humanNum)*2
saveEarthNum = totalAlienNum - totalHumanNum - 2
if saveEarthNum >= 0:
    print(saveEarthNum)
else:
    print('Big Bang!')

