# for x in reversed(a):
#     print(x)

class Countdown:
    def __init__(self,start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

if __name__ == '__main__':
    a = Countdown(4)
    for x in Countdown.__reversed__(a):
        print(x)