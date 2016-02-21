from clientpy2 import run, subscribe
import operator

cash = "MY_CASH"
name = "Excelsior"
code = "C0d3c0n2016"

dividends = open("dividends.csv", "r")
blacklist = []

def getMaxDiv():

    divs = str(run("Excelsior", "C0d3c0n2016", "SECURITIES")).split()
    del divs[0]
    names = []
    vals = []
    i = 0
    while i < len(divs) - 2:
        names.append(divs[i])
        vals.append(float(divs[i + 2]))
        i+=4

    i = 0
    while i < len(names):
        i+= 1

    index, value = max(enumerate(vals), key=operator.itemgetter(1))

    return names[index], value


print getMaxDiv()

def bidAskTicker(ticker):
    orderData = run(name, code, "ORDERS " + ticker);
    # print ticker
    # print orderData
    orderData = orderData.split()[1:]
    # print(orderData)
    bidIndices = [i for i, x in enumerate(orderData) if x == "BID"]
    askIndices = [i for i, x in enumerate(orderData) if x == "ASK"]
    maxBid = -1
    lowestAsk = -1
    if(len(askIndices) > 0):
        lowestAsk = orderData[askIndices[0] + 2]
    if(len(bidIndices) > 0):
        maxBid = orderData[bidIndices[0] + 2]
    for i in range(1, len(bidIndices)):
        newBid = float(orderData[bidIndices[i] + 2])
        if(newBid >= maxBid):
            maxBid = newBid
    for i in range(1, len(askIndices)):
        newAsk = float(orderData[askIndices[i] + 2])
        if(newAsk <= lowestAsk):
            lowestAsk = newAsk
    return (maxBid, lowestAsk)

print bidAskTicker(getMaxDiv()[0])
while True:
    print bidAskTicker(getMaxDiv()[0])
    print run(name, code, "BID " + getMaxDiv()[0] + " " +
     str(float(bidAskTicker(getMaxDiv()[0])[1]) + .05)  + " " +
     str(float(run(name, code, "MY_CASH").split()[1]) / float(bidAskTicker(getMaxDiv()[0])[1]) ) )
