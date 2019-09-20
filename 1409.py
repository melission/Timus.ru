inp = input()
Harry, Larry = inp.split()
totcans = int(Larry)+int(Harry)-1
totHarry = totcans - int(Harry)
totLarry = totcans - int(Larry)
if totHarry < 0:
    totHarry = 0
if totLarry < 0:
    totLarry = 0
print(totHarry, totLarry)