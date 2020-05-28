import csv

with open("/Users/MAC/Downloads/stocks.csv") as f:
    f_csv = csv.reader(f)
    # print(f_csv)            #<_csv.reader object at 0x1110a89e8>
    # print(type(f_csv))      #<class '_csv.reader'>
    headers = next(f_csv)
    # print(headers)          #['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
    # print(type(headers))    #<class 'list'>
    for row in f_csv:
        print(row[0])

