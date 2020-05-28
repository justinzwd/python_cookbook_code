from collections import deque

def search(lines,pattern,history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line,previous_lines
        previous_lines.append(line)

if __name__ == '__main__':
    with open('1.txt') as f:
        for line,prevlines in search(f,'python',5): #search()方法返回的结果是line,previous_lines
            for pline in prevlines:
                print(pline,end='') #这两句决定了打印的顺序
            print(line,end='')
            print('-'*20)
