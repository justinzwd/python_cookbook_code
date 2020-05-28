import os

files = os.listdir('dirname')
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('sorry, no python!')

#output a tuple as csv
s = ('ACME',50,123.45)
print(','.join(str(x) for x in s))

#Data redution across fields of a data structure
portfolio = [
    {'name':'GOOG','shares':50},
    {'name':'YHOO','shares':75},
    {'name':'AOL','shares':20},
    {'name':'SCOX','shares':65}
]

min_shares = min(s['share'] for s in portfolio)
