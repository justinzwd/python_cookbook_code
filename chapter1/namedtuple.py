from collections import namedtuple

Stock = namedtuple('Stock',['name','shares','prices','date','time'])

# create a prototype instance

stock_prototype = Stock('',0,0.0,None,None)

# Function to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)

a = {'name':'ACME','shares':100,'prices':123.45}

print(dict_to_stock(a))

b = {'name':'ACME','shares':100,'prices':123.45,'date':'12/17/2012'}
print(dict_to_stock(b))
