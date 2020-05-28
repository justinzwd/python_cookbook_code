# read the entire file as a single string
# with open('somefile','rt') as f:
#     data = f.read()

# iterate over the lines of the file
# with open('somefile','rt'):
#     for line in f:
#         #process line
#         ...

# write chunks of text data
# with open('somefile.txt','wt') as f:
#     f.write(text1)
#     f.write(text2)

# redirected print statement
# with open('somefile.txt','wt') as f:
#     print(line1,file=f)
#     print(line2,file=f)

# f = open('somefile.txt','rt')
# data = f.read()
# f.close()

"""
f = open('hello.txt','rt')
print(f.read())

# newline translation disabled
g = open('hello.txt','rt',newline='')
print(g.read())
"""

# f = open('hello.txt','rt',encoding='latin-1')
# print(f.read())

# print('ACME',50,91.4)
# print('ACME',50,91.4,sep=',')
# print('ACME',50,91.4,sep=',',end='!!\n')

# for i in range(5):
#     print(i,end=' ')


# print(','.join(('ACME','50','97.2')))

# row = ('dfdfj','79','89.3')
# print(','.join(row))

# print(*row,sep=',')

# read the entire file as a single byte string
# with open('somefile.bin','rb') as f:
#     data = f.read()

# write binary data to a file
# with open('somefile.bin','wb') as f:
#     f.write(b'helloworld')