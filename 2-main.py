import math
import random
from math import pi
s1 = str()
print(type(s1))

s2 = str([1,2,3])
print(s2)

s3 = "this is a string"
print(type(s2))

s4 = "python"
print(type(s3))

s5 = '''this is string'''
print(type(s5))

'''
st1, st2, st3 = 'python', 'proggramming', '*'
print('length of st1 is: ', len(st1))
print('substring of st1: ', st2[:4])
print('st1 + st2: ', st1 + st2)
print('15 * st3: ', 15 * st3)
for i in st2:
    print(i, end = ' ')
   
    ----------------

x = ord('A')
y = chr(65)

print("x: ", x)
print("y: ", y)

 -----------------


x = "this, is a split, using for, python labs"

print(x.split())

print(x.split(','))

 ---------------




arr = ['this', 'is', 'a','string', 'using', 'for', 'python', 'labs']

print(' '.join(arr))

print(' -> '.join(arr))


--------------------------


x  = "1*Python Programming!****7"
print(f"Before using strip() : {x}")
print(f"After using strip(): {x.strip('1*7')}")


txt = ",,,,,rrttgg.....banana....rrr"

x = txt.strip(",.grt")

print(x)

x = "*****Python Programming!*****"
print(f"Count of '*' symbols in '{x}' is {x.count('*')}")


----------------------


x = "python programming"
print(f"before: {x}\n After: {x.title()}")


-------------------------

x = "python programming"

print(f"Substring 'prog' starts at position:  {x.find('prog')}")

answer = print(f"Substring 'c++' starts at position: {x.find('c++')}")

if answer == True:
    print("yes")
else:
    print("error")


    -----------------------------


x = "python programming"

print(f"Substring 'prog' starts at position:  {x.index('prog')}")

answer = print(f"Substring 'c++' starts at position: {x.index('c++')}")


---------------------


st, st1, st2 = 'python programming', 'pyth', 'prog'

print(f"String starts with substring '{st1}': {st.startswith(st1)}")

print(f"String starts with substring '{st2}': {st.startswith(st2)}")

print(f"String starts with substring '{st2}' at position 7: {st.startswith(st2,7)}")


----------------------


soz, soz1, soz2 = 'sabir', 'sabir aliyev', 'sabir aliyev uzeyir oglu'

print(f"String starts with substring {soz} : {soz2.startswith(soz)}")

print(f"String starts with substring {soz1} : {soz2.startswith(soz1)}")

print(f"String starts with substring {soz2} : {soz.startswith(soz2)}")

print(f"String starts with substring {soz1} : {soz.startswith(soz1)}")


--------------------


st, st1, st2 = 'python programming', 'ming', 'thon'

print(f"String ends with substring '{st1}' : {st.endswith(st1)}")

print(f"String ends with substring '{st2}' : {st.endswith(st2)}")

print(f"String ends with substring '{st2}' at part [0,6]: {st.endswith(st2, 0, 6)}")


-------------------

st = 'python programming'

print("before using methodd replace(): ", st)
print(f"After using method replace(): {st.replace('p','P')}")
print(f"After using method replace(): {st.replace('p','@')}") 


-----------------


mesaj = input("bir string giriniz: ")
arr = ['a','b','c','d']

for n in arr:
    if mesaj.startswith(n):
        print(f"stringiniz {n} harfiyle basliyor") 
        break
    else:
        print(f"yazdiginiz soz {n} harfiyle baslamiyor")

-----------------


mesaj = input("Bir string giriniz: ")
arr = ['a', 'b', 'c', 'd']

baslayan = []
baslamayan = []

for n in arr:
    if mesaj.startswith(n):
        baslayan.append(n)
    else:
        baslamayan.append(n)

if baslayan:
    print(f"Stringiniz bu harflerle basliyor: {baslayan}")
if baslamayan:
    print(f"Stringiniz bu harflerle baslamiyor: {baslamayan}")

   ---------------
    
input("string girin: ")
soz = "sabir"

answer = soz.replace('s', '$')
print(answer)


 ----------------

print(f"'Python3' contains only alphabet symbol: {'Python3'.isalpha()}")
print(f" 'Pyt hon' contains only alphabet symbol: {'pyt hon'.isalpha()}")
print(f"'Python' contains only alphabet symbol: {'Python'.isalpha()}")


 -------------------

print(f"'123abc' contains only alphabet symbol: {'123abc'.isdigit()}")
print(f"'12345' contains only digits: {'12345'.isdigit()}")


----------------



print("Empty object: ", bytes())
a = bytes("Python", "utf-8")
print("value of a: ", a)
print(f"Type of {a}: {type(a)}")


-----------------

a = "Python".encode()
print("Sequence of bytes: ", a)
print(f"Type of {a}: {type(a)}")


---------------

a = b'Python'
print("Sequence of bytes: ", a)
print(f"Type of {a}: {type(a)}")


-----------------


x = b'Python'
print(f"Type of x is: {type(x)}")
print(f"type of y is: {type(x.decode())}")
 
--------------

print("Empty object: ", bytearray())  
a = bytearray("Python", "utf-8")
print("value of a: ", a)
print(f"Type of a: {type(a)}")


---------------------

barr = bytearray('Python', 'utf-8')
print("Before using method append: ", barr)
barr.append(b'123'[1])
print("After using method append: ", barr)


------------------

soz = bytearray("sabir", "utf-8")
print("Before using method append: ", soz)
soz.append(b"aliyev"[0])
print("after using method append: ", soz)
soz.extend(b" ")
soz.extend(b"aliyev")
print("after using method extend: ", soz)


------------

barr = bytearray('Python', 'utf-8')
print(f"Before using method insert: {barr}")
barr.insert(4, b'123'[1])
print(f"After using method insert: {barr}")

------------

soz = bytearray("sabi", "utf-8")
print(f"before using method insert {soz}")
soz.insert(4, b"rggbrear"[0])
print(f"after using method insert {soz}")

------------

barr = bytearray("Python", "utf-8")
print("before using method pop: ", barr)
x = barr.pop(3)
print(f"After using method pop: {barr}")
print(f"ASCII code: {x}\nCharacter value: {chr(x)}")
print(f"the word: {barr}")


---------------


barr = bytearray('Python Programming', 'utf-8')
print("Before using method remove: ", barr)
barr.remove(b'ojftdtfdj'[0])
print("After using method remove: ", barr)


------------

barr = bytearray('python', 'utf-8')
print("before using method reverse: ", barr)
barr.reverse()
print("after using method reverse: ", barr)


---------------


# print(math.pi)

#print(math.e)

#print(math.sin(1))
#print(math.cos(1))
#print(math.tan(1))

x = math.sqrt(169)
print(x)

print(math.ceil(3.67))
print(math.floor(3.67))

print(math.pow(3,4))

print(math.fmod(-11, 5))


--------------


random.random()

#print(random.uniform(0,10))

#print(random.randint(0, 10))

#print(random.choices("Python"))

print(random.choices([1,2,3,4,5,6]))

arr = [1,2,3,4,5,6,7]
random.shuffle(arr);
print(arr)


random.sample(arr,3)
print(arr)

 
------------------


text = input("enter string:\n")

sentences = [s.strip() for s in text.split('.') if s.strip()]

print("Bulunan cumle sayisi: ", len(sentences))


-------------


text = input("Metin giriniz: ")
parcalar = text.split('.')

temizlenmis = []

for s in parcalar:
    temizlenmis_soz = s.strip()

    if temizlenmis_soz != "":
        temizlenmis.append(temizlenmis_soz)

sentences = temizlenmis

print("Bulunan cumle sayisi:", len(sentences))


---------------------


text = input("enter sentences: ")

sentences = [s.strip() for s in text.split('.') if s.strip()]

max_sentences = ""
max_count = 0

for s in sentences:
    count = s.count('x')
    if count > max_count:
        max_count = count
        max_sentences = s

if max_sentences:
    print(f"en cox 'x' olan cumle: {max_sentences}")
    print(f"'x' sayisi: {max_count}")
else:
    print("hec bir cumlede 'x' tapilmadi.")

    -----------------

cumle = input("bir cumle giriniz: ")

parcalar = cumle.split('.')

temizlenmis = []
max_sentence = ""
max_count = 0
for s in parcalar:
    temizlenmis_soz = s.strip()

    if temizlenmis_soz != "":
        temizlenmis.append(temizlenmis_soz)
    
cumleler = temizlenmis

print("bulunan cumle sayisi", len(cumleler))

for n in cumleler:
    count = n.count('x')
    if count > max_count:
        max_count = count
        max_sentence = n

if max_sentence:
    print(f"en cok 'x' olan cumle: {max_sentence}")
    print(f"'x' sayisi: {max_count}")
else:
    print("hec bir cumlede 'x' tapilmadi")


    -------------------

text = input("enter your text: ")

parcalanmis_cumleler = text.split('.')

arr_cumleler = []

for n in parcalanmis_cumleler:
    arr_cumleler.append(n)

max_word = arr_cumleler[0]

for x in arr_cumleler:
    if len(x.split()) > len(max_word.split()):
        max_word = x

print("en cok soze sahip olan cumle: ", max_word)

'''

