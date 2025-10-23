'''
x = int(input("enter you number:"))

if x % 5 == 0:
    print(str(x) + " mod 5 is 0")
elif x % 5 == 1:
    print(str(x) + " mod 5 is 1")
elif x % 5 == 2:
    print(str(x) + " mod 5 is 2")
elif x % 5 == 3:
    print(str(x) + " mod 5 is 3")
elif x % 5 == 4:
    print(str(x) + " mod 5 is 4")

-------------------- 

x = int(input('Enter integer number: '))

if x%2 == 0:
    print(str(x) + " is oven")
else:
    print(str(x) + " is odd")
    
    -------------------

x = int(input("enter you number:"))

if x % 5 == 0:
    print(str(x) + " mod 5 is 0")
elif x % 5 == 1:
    print(str(x) + " mod 5 is 1")
elif x % 5 == 2:
    print(str(x) + " mod 5 is 2")
elif x % 5 == 3:
    print(str(x) + " mod 5 is 3")
else:
    print(str(x) + " mod 5 is 4")

   
    
st = input("enter string: ")
for s in st:
    print(s)

    --------------------

arr = [1,2,3,4,5,6,7,8]
i = 0
while i < len(arr):
    print(arr[i], end = ' ')
    i = i + 1

      ------------------

arr = input("enter array's elements: ")

for x in list(arr):
    print(x, end=' ')

     ------------------

random = range(1,11)

for x in random:
    print(x**2, end = ' ')

     ----------------------

arr = [1,2,3,4,5,6,7,8,9,10]
for ind, elem in enumerate(arr):
    if elem % 2 == 0:
        arr[ind] **= 2
print(arr, end = " ")
 
-----------------------------

arr = [10,11,12,13,14,15,16,17,18,19,20]

for i in range(11):
    if arr[i] % 3 == 0:
        continue
    if arr[i] % 3 == 1:
        arr[i] *= 2
        continue
    if arr[i] % 3 == 2:
        arr[i] *= 3
print(arr)


 ------------------------

arr = [10,11,12,13,14,15,16,17,18,19,20]

size = len(arr)
for ind in range(size):
    print(ind)
    if arr[ind] == 14:
        break
    if size != ind:
        print("Element exist")
    else:
        print("Element not exist")

        
        -----------------------------
 

arr = [1,2,3,4,5,6,7,8,9,10]

size = len(arr)

for ind in range(size):
    print(ind)
    if arr[ind] == 5:
        print(arr[ind])
        break
    if size != ind:
        print("element exist")
    else:
        print("element not exist") 

        ------------------------

       

x  = int(input("enter first number: "))
y = int(input("enter second number: "))

print("+, -, *, / ")
method = input("enter method: ")

if method == "+":
    print(x+y)
elif method == "-":
    print(x-y)
elif method == "*":
    print(x*y)
elif method == "/":
    if y == 0:
        print("error")
    else:
        print(x/y)


        -------------------------

integers = range(20,51)
numbers_divisible_7 = []
for i in integers:
    if i % 7 == 0:
        numbers_divisible_7.append(i)

print("number divisible by 7: ",numbers_divisible_7)
product = 1
for x in numbers_divisible_7:
    cube = x*x*x
    print("Cube of", x, "is", cube)
    product = product * cube
print("7 nin katlarinin kuplerinin carpimi: ", product)


 
-------------------------


arr = range(20,50)
digit_sum_7 = []
for i in arr:
    digit_sum = 0
    for digit in str(i):
        digit_sum += int(digit)
    if digit_sum == 7:
        digit_sum_7.append(i)
sum = 0
for x in digit_sum_7:
    sum = sum + x
average = sum / len(digit_sum_7)

print("Rakamlarinin toplami 7ye esit olan sayilar: ", digit_sum_7)
print("7-ye bolunen sayilarin toplami: ", sum)
print("7-ye bolunen sayilarin aritmetik ortalamasi: ", average)


'''
import math

a = float(input("enter first number: "))
b = float(input("enter second number: "))
c = float(input("enter third number: "))

discreminant  = b**2 - 4*a*c

if discreminant > 0:
    x1 = (-b + math.sqrt(discreminant)) / (2*a)
    x2 = (-b - math.sqrt(discreminant)) / (2*a)
    print("denklemin iki koku var: ")
    print("x1 = ", x1)
    print("x2 = ", x2)

elif discreminant == 0:
    x12 = (-b + 0) / (2*a)
    print("denklemin bir koku var: ")
    print("x1,2 = ", x12)

else:
    print("discreminant < 0")
    print("denklemin koku hic yok!")