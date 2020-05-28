iterms = [1,10,5,4,7]



# print(head)

def sum(iterms):
    head, *tail = iterms
    return head + sum(tail) if tail else head

print(sum(iterms))      #input: 27