class Info:
    def __init__(self,name,n):
        self.name = name
        self.n = n

s = '{name} has {n} messages'
a = Info('Guido',37)
print(s.format_map(vars(a)))
