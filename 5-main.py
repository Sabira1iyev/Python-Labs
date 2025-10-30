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

------------

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

------

f = open(file = 'data_txt.txt', mode = 'r')
s = f.read()
print(s)
f.close()


------------

f = open(file = 'data_binary.txt', mode = 'w')
x = ("hello")
y = f.write(x);
print('Count of recorded bytes is ', y)
f.close()

---------

f = open(file = 'data_binary.txt', mode = 'r')
s = f.read()
print(s)
f.close()


-----------------

f = open(file='data_txt.txt', mode = 'w', encoding = 'utf-8')
lst = ['es ' , 'striqoni ', 'chaiwereba ', 'failshi ']
lst1 = ['es ', 'striqoni ', 'chaiwereba ', 'failshi']
f.writelines(lst)
f.writelines(lst1)
f.close()

f = open(file = 'data_txt.txt', mode = 'r', encoding = 'utf-8')
s = f.read()
f.close()


------------


f = open(file = "data_binary.txt", mode = 'wb')
lst = ['es '.encode('utf-8'), 'striqoni '.encode('utf-8'),
       'chaiwereba '.encode('utf-8'), 'failshi '.encode('utf-8')]
y = f.writelines(lst);

----------

f = open(file = 'data_txt.txt', mode ='r', encoding='utf-8')
print('f file is open in write mode: ', f.writable())


------------

f = open(file= 'data_txt.txt', mode = 'r', encoding='utf-8')
print('read file fully: ', f.read())
f.close()
f = open(file='data_txt.txt', mode = 'rb')
st = f.read()
print('read only 7 byte', st.decode());


-------------


arr = []
for  i in range(1,11,1):
    f = open(file = 'data_txt.txt', mode='r', encoding='utf-8')
    print('read only 7 byte', f.read(i*7));
    arr.append(f.read(7))

    '''


f = open(file = 'data_txt.txt', mode='r', encoding='utf-8')
print('first: using readline : ', f.readline())
print('second: using readline : ', f.readline())
print('third: using readline : ', f.readline())
print('fourth: using readline : ', f.readline())