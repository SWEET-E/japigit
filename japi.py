#Evan Dieterich IFT 458 PD5 10/13/20
#myapikey = 'PGEHE24MBY1ZUPQA'

import json
import sys
import urllib.request

def getStockData(symbol) :
    symbol = symbol
    url = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=" + symbol + "&apikey=PGEHE24MBY1ZUPQA"
    connection = urllib.request.urlopen(url)
    responseString = connection.read().decode()
    return responseString

def main():
    while True:
        print("Enter a stock symbol or type quit: ", end="")
        symbol = input().upper()
        if symbol == "QUIT":
            sys.exit(0)
        elif symbol == "":
            sys.exit(0)
        else:
            print(getStockData(symbol))
            get = json.loads(getStockData(symbol))
            print("The current price of " + get["Global Quote"]["01. symbol"] + " is: $" + get["Global Quote"]["05. price"]
                  + " as of " +get["Global Quote"]["07. latest trading day"])
            with open('japi.out', 'a') as f:
                print(getStockData(symbol), file=f)
def success():
    return print("Stock quotes retrieved successfuly!")

if __name__ == "__main__":
    main()
    success()
