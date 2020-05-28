d = {
    'a' : [1,2,3],
    'b': [4,5]
}

e = {
    'a' : {1,2,3},
    'b' : {4,5}
}

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(3)
d['a'].append(3)        #允许有重复值
d['a'].append(4)
d['b'].append(4)
d['b'].append(5)

print(d)

e = defaultdict(set)
e['a'].add(1)
e['a'].add(2)
e['a'].add(3)       #不允许有重复值
e['a'].add(3)
e['a'].add(4)
e['b'].add(4)
e['b'].add(5)

print(e)