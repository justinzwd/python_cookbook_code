import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self,item,priority):
        heapq.heappush(self._queue,(-priority,self._index,item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self,name):
        self.name = name
        def __repr_(self):
            return 'Item({!r})'.format(self.name)

if __name__ == '__main__':
    q = PriorityQueue()
    q.push(Item('foo'),1)
    q.push(Item('bar'),5)
    q.push(Item('spam'),4)
    q.push(Item('grok'),1)

    # print(q.pop().name)
    # print(q.pop().name)
    # print(q.pop().name)
    # print(q.pop().name)

    a = (1, Item('fooz'))
    b = (5,Item('bar'))
    print(a<b)
    c = (1,Item('grok'))
    # print(a<c)
