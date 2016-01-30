from time import sleep
from clientpy2 import run, subscribe

cash = "MY_CASH"

worth = open("worth.csv", "w")
dividend = open("dividends.csv", "w")
volatility = open("volatility.csv", "w")

def initialize():
    data = str(run("Excelsior", "C0d3c0n2016", "SECURITIES")). split()
    del data[0]
    print data
    i = 0
    while i < len(data) - 1:
        worth.write(data[i] + ", ")
        dividend.write(data[i] + ", ")
        volatility.write(data[i] + ", ")
        i = i + 4
    worth.write("\n")
    dividend.write("\n")
    volatility.write("\n")


initialize()
while True:
    data = str(run("Excelsior", "C0d3c0n2016", "SECURITIES")). split()
    del data[0]
    i = 0
    while i < len(data) - 1:
        worth.write(data[i + 1] + ", ")
        dividend.write(data[i + 2] + ", ")
        volatility.write(data[i + 3] + ", ")
        i += 4
    worth.write("\n")
    dividend.write("\n")
    volatility.write("\n")

