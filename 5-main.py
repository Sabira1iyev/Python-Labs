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



arr = ['ha','wa','ka']
for i in range(3):
    f = open(file = 'data.txt', mode = 'w+')
    f.write(arr[i])
f.close()

e = open(file = 'data.txt', mode = 'r')
s = e.readline()
print(s)
e.close()

-----------

f = open(file = 'data_txt.txt', mode='w', encoding = 'utf=8')
y = f.write("es striqoni chaiwereba failshi");
print('count of recorded elements is', y)
f.close()

---------

fayl = open(file = 'data_txt.txt', mode = 'w')
y = input("enter information abobut you: ")
yazdir = fayl.write(y)
print("count of recorded elements, which you writed ->", yazdir)
fayl.close()

------------

f = open(file='data_txt.txt', mode = 'r')
s = f.read()
print(s)
f.close()

---------


f = open(file = 'data_binary.txt', mode = 'wb')
x = 'es striqoni chaiwereba failshi' .encode('utf-8')
y = f.write(x);
print('Count of recored bytes is ', y)
f.close()

'''

# TEXT MODE

f = open('text_mode.txt', 'w', encoding='utf-8')
text = "Hello Sabir"
count_text = f.write(text)
f.close()
print('text modda yazilan karakter sayisi: ', count_text)


# BINARY MODE

f = open('binary_mode.txt', 'wb')
binary_data = text.encode('utf-8')
count_bin = f.write(binary_data)
f.close()
print("Binary modda yazilan byte sayisi: ", count_bin)

r = open('data_binary.txt', mode='rb')
data = r.read()
print(data)
r.close()