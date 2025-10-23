import time
import random
import math
'''
 

array1 = []

array1.append(12)
array1.append("hello")
array1.append([13,14])
array1.append(None)

print(array1)

array1[3] = 5
print(array1)

 ----------


arr = []

arr.append(1)
arr.append(2)
arr.append(3)

x,y,z = arr

print(x,y,z)

--------------
 

array = list([1,2,3,4,5,6])

x, *y, z = array

print(x,y,z)

print(f"siashi sami elementis raodenoba tolia: {len(array)} - is")


print(array[0])
print(array[-2])

-----------

arr = []
for i in range(15):
    arr.append(i)
print(arr)

print(arr[:3])
print(arr[2:8])
print(arr[5:])
print(arr[::-1])
print(arr[::2])


 ---------------

arr = [1,2,3,4,5,6,7,8]

if 3 in arr:
    print("3 is in arr")
if 10 not in arr:
    print("10 is not in arr")


random.shuffle(arr)

t1 = time.time()
for i in arr:
    if i ==3:
        print("hello")
t2 = time.time()
t3 = time.time()

if 3 in arr:
    print("hello")
t4 = time.time()

print(t2-t1)
print(t4-t3)
print(t3==t2)


-----------------


arr = []

for i in range(5):
    a = []
    for j in range(5):
        x = random.randint(0,1000)
        a.append(x)
        arr.append(a)
MAX = 0
for i in range(5):
    for j in range(5):
        if MAX < arr[i][j]:
            MAX = arr[i][j]
for i in range(5):
    print(arr[i])
print("\nmax value in arr is ", MAX)
print(type(arr))

-------------

c = []
a = [1,2,3,4]
b = [5,6,7]
c.append(a)
c.append(b)
c.append(3)
print(c)
print(type(c))


--------------


arr = []

arr.append(1)
arr.append(12)
arr.append(4)
print(arr)

-------------


arr = [1,2,3,4,5]
print(f"Before using extend(): {arr}")
arr.extend([6,7,8,9])
print(f"after using extend: {arr}")

 
-------------

arr = [1,2,3,4,5]
arr.insert(2, 10)
print(f"after using insert: {arr}")

---------------

arr = [1,2,3,4,5,6,7,8,9]
print(arr.pop())
print(f"aster using pop: {arr}")
arr.pop(3)
print(f"aster using pop: {arr}")


--------------------

arr = [random.randint(1,200) for _ in range(100)]
print(f"arr.index(50) = {arr.index(50)}")
if 1000 in arr:
    print(f"arr.index(1000) = {arr.index(1000)}")
else:
    print("Object does not exists")


------------

arr = [1,2,3,4,3,6,7,3,3]
print(f"arr.count(3) = {arr.count(3)}")
print(f"arr.count(10) = {arr.count(10)}")

---------

arr = [1,2,3,4,0, None,6,7,8,9]
print(f"any(arr) = {any(arr)}")
print(f"all(arr) = {all(arr)}")

----------

arr = [1,2,3,4,5,6,7,8,9]
print(f"random.choice(arr) = {random.choice(arr)}")


---------------

arr = [1,2,3,4,5,6,7,8,9]
print(f"two object from list: {random.sample(arr, 2)}")
print(f"four object from list: {random.sample(arr, 4)}")


----------------


## DICTIONARY       

dict1 = dict()
print(type(dict1))

dict2 = dict(a = 1, b = 2)
print(dict, dict2)
dict3 = dict([['a', 1], ['b', 2]])
dict4 = dict([('a',1), ('b', 2)])
print(dict3, dict4)


-------------


dict2 = {}
print(type(dict2))


--------------


d = {'a': 1, 'b':2}
print(f"Element by key: 'a': {d["a"]}")
print(f"Element by key: 'b': {d['b']}")

 ----------------

d = {'a': 1, 'b':2}

if 'a' in d:
    print(f"element by key 'a': d['a']")
else:
    print('key a does not exists: ')
if 'c' not in d:
    print('key c does not exists: ')
else:
    print(f"element by key 'c': {d['c']}")

-------------

d = {'a': 1, 'b':2}
for key in d:
    print(f'key= {key}, value= {d[key]}')
    
print(type(d.keys()))


-----------------

d = {'a': 1, 'a':1,'b': 2}
for key in d:
    print(f"key = {key}, value= {d[key]}")
print(len(d.keys()))


---------------


d = {'a': 1, 'b':2}
for v in d.values():
    print(f'value = {v}')

--------------

d = {'a':1,'b':2}
for v in d.items():
    print(v)

    -----------

d = {'a':1, 'b':2, 'c':3, 'd':4}
for k,v in d.items():
    print(k,v)

    
d = {'a':1,'b':2}
print(d.get('e'), d.get('c'))

-----------

d = {'a':1, 'b':2}
print(d.get(1, 'python'), d.get('c'))

---------------

d = {'a':1, 'b': 2}
print(d.pop('a'))
print(d.pop('a', 'aseti gasawebi leqsikoni araa'))

--------------

d = {'a':1, 'b':2}
print(d.clear())


--------------

d = {'a':1, 'b': 2}
d.update({'a':3})
for key in d:
    d.update({'c':3})
    print(f"key= {key}, value= {d[key]}")

    -------------

arr = [1,2,4,5]
for i in arr:
    a = arr[:]
    print(i)
    if i == 3:
        arr.remove(i)

        --------------

d = {'a':1, 'b':2}
print("before update: ")
for key in d:
    print(f"key = {key}, value = {d[key]}")
print()
d.update({'a':3})
print("after update ")
for key in d:
    print(f"key= {key}, value = {d[key]}")

     -------------

tup1 = tuple()
print(f'Empty tuple')
tup2 = tuple('Python')
print(f'tuple has values: {tup2}')
tup3 = tuple([1,2,3,4,5])
print(f'tuple has values: {tup3}')


------------------

tup1 = ()
tup2 = (1)

tup3 =(1,'str', (1,2), [1,2])
print(f"empty tuple = {tup1}")
print(f"one object tuple: tup2 = {tup2}")
print(f"tuple with different type objects: tup3 = {tup3}")


--------------

a = [1,2,3]
t = (1,a,4)
print(t)
a.append(5)
print(t)

------------

print('get range by step 10:')
for i in range(1,101, 10):
    print(i, end = ' ')
print()
print('get list: arr')
arr = [i** 2 for i in range(1,11)]
print('\t', arr)
print('get dictionary:')
dct = {key : key ** 3 for key in range(1,6)}
for key in dct.keys():
    print(f'\tkey = {key}, \tvalue = {dct[key]}')

   ----------------------


s1 = set()
s2 = set('Python programming')
s3 = set((1,2,3,4,5))
s4 = set([1,2,3,4,5])

print(f'Empty set: set = {s1}')
print(f'set from string: \ns2 = {s2}')
print(f'set from tuple : s2 = {s3}')
print(f'set from list: s4 = {s4}')

--------------


s = set((1,2,4,5,1,3,2,5,3,4,5))
print(f'set has {len(s)} elements')
print('set s has element: ', end=' ')
for i in s:
    print(i, end=' ')

--------------------


q = set((1,2))
e = set(((100,20,1,5), "1", (100,20,3), 66, d))


    ---------------


a = set((1,2,4,5,1,3,2,5,3,4,5))
b = set((1,4,9,16,25,36,49,64,81,100))

print()
c = a.union(b)
print(c)
print(type(c))
c.add(500)
print(c)
print(type(c))


------------
 
a = set((4,6,3,1,9))
b = set((1,4,9,16,25,36,49,64,81,100))
print(a)
a.add(2)
print(a)


a.update(b)
print(a)

---------------

 

a = set((4,6,3,1,9))
b = set((1,4,9,16,25,36,49,64,81,100))

print(f"set a{a}")
print(f"set b {b}")
a = a.difference(b)
print(a)

------------------
 

a = set((4,6,3,1,9))
b = set((1,4,9,16,25,36,49,64,81,100))
a = a.intersection(b)
print(a)

 ---------------

arr = []

for i in range(20):
    arr.append(random.randint(1,100));
print(arr)

----------------


arr = []

while len(arr) < 25:
    num = random.randint(15,75)
    if num not in arr:
        arr.append(num)
print("List: ", arr)

product = 1
for n in arr:
    product *= n

print("elementebis namravli = ", product)


 -----------------

arr = []

for i in range(25):
    if i not in arr:
        arr.append(random.randint(15,75))

print(arr)


-------------


arr = []

while len(arr) < 25:
    num = random.randint(15,75)
    if num not in arr:
        arr.append(num)
print(arr)

'''
arr1 = []
arr = [random.randint(100000, 1000000) for _ in range(1000)]
arr1 = [x for x in arr if x % 17 == 0 and str(x)[-1] not in ('5','7')]

filtered = [x for x in arr if sum(int(d) for d in str(x)) % 2 == 0 and str(x)[-1] not in('3','7')]

first_500 = filtered[:500]
print("ilk 20 sayi: ", arr1[:20])

print("ilk 20 sayinin kareleri toplami: ", sum(x**2 for x in arr1[:20]))
