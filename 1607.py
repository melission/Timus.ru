
customerPrice, customerProposal, driverPrice, driverProposal = input().strip().split()
customerPrice, customerProposal = int(customerPrice), int(customerProposal)
driverPrice, driverProposal = int(driverPrice), int(driverProposal)

finishPrice = 0
changed = True
acc = True
if customerPrice > driverPrice:
    finishPrice = customerPrice
    acc = False
while acc:
    if customerPrice + customerProposal < driverPrice:
        customerPrice = customerPrice + customerProposal
        finishPrice = customerPrice
            # print(customerPrice)

    if customerPrice + customerProposal > driverPrice:
        finishPrice = driverPrice
    if customerPrice + customerProposal < driverPrice:
        driverPrice = driverPrice - driverProposal
        finishPrice = driverPrice
            # print(driverPrice)
    else:
        acc = False


print(finishPrice)
