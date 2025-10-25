from os.path import abspath
# print(abspath('main.py'))

# x = open(file = 'data.in', mode='r', encoding = 'utf-8')

'''
f = open(file ='data.txt', mode = 'w+')
f.write('hello')
fa= f.readline()
f.close()
print(fa)

---------------


'''

arr = ['ha','wa','ka']
for i in range(3):
    f = open(file = 'data.txt', mode = 'w+')
    f.write(arr[i])
f.close()

e = open(file = 'data.txt', mode = 'r')
s = e.readline()
print(s)
e.close()