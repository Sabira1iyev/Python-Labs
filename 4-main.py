import time

'''
def my_func():
    pass

    ----------

def my_func(a):
    print(a)

my_func(1)


----------


def greater(a,b):
    if a > b:
        print(  "a greater than b")
    elif a < b:
        print("b greater than a")
    else:
        print("they are same integers")
greater(3,4)

-------


def a_and_b(a,b):
    return a+b, a*b

x, *y = a_and_b(2,7)
print(f"x is {x}, y is{y}")

----------

def sayilar(a,b):
    return a+b, a*b, a - b, a/b

x, y = sayilar(10,5)
print(f"x = {x}, y = {y}")

x, *y = sayilar(10,5)
print(f"x = {x}, y = {y}")

------

def user_func(a, b = 2):
    return a + b
print(user_func(1))
print(user_func(1,9))

---------

def user_func(*, a,b, c=10):
    return a+ b+c
#c = user_func(1,2,1)
#c = user_func(a = 1, b=5)
print(c)

------

def Sum(*t):
    summ = 0
    for i in t:
        summ += i
    return summ
print(f"Zero parameter: Sum() = {Sum()}")
print(f"Two parameter: sum(10,20) = {Sum(10,20)}")
print(f"Threee parameter: sum(10,20,30) = {Sum(10,20,30)}")

--------

def Sum(**t):
    summ = 0
    for i in t.keys():
        summ += t[i]
    return summ
print(Sum())
print(Sum(x = 10, y = 20))
print(Sum(a=10,b=20,c=30))

---------

def Sum(**t):
    summ = 0;
    for i in t.values():
        summ += i
    return summ
print(Sum())
print(Sum(x = 10, y= 20))
print(Sum(a = 10, b= 20, c= 30))

--------

def Sum(**t):
    summ = 0
    for key,value in t.items():
        summ += value
    return summ
print(Sum())
print(Sum(x = 10, y=20))
print(Sum(a=10,b=20,c=30))


----------

def Sum(a,b):
    return a + b

def print_sum(f,a,b):
    print(f"{a} + {b} = {f(a,b)}")

print_sum(Sum,1,2)

------------

def print_sum(a,b):
    def Sum():
        return a+ b
    print(f"{a} + {b} = {Sum()}")
    return Sum
print(print_sum(1,2))


--------------

def bank_account(balance):
    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance
    def withdraw(amount):
        nonlocal balance
        balance -= amount
        return balance
    return deposit, withdraw

deposit, withdraw = bank_account(100)
print(deposit(50))
print(withdraw(25))


------------


printinfo = lambda: print("This is lambda function")
summ = lambda x,y: [x+y,x*y]
printinfo()
summ_result = summ(10,23)
print(f"summ = {summ_result}")


---------------

def choose(struct):
    return struct[1]

people = [("Ana", 24), ("Nino", 30), ("Giorgi", 20)]
sorted_people = sorted(people, key=choose)
print(sorted_people)

------------


sum1 = lambda x,y: x+y
def sum2(x,y):
    return x+ y
t1= time.time()
sum1(1,2)
t2 = time.time()
t3 = time.time()
sum2(1,2)
t4 = time.time()
print(t2-t1)
print(t4-t3)


---------------

def func_gen(x,y):
    for number in range(x+1):
        yield number ** y

numbers = func_gen(10,2)
for n in numbers:
    print(n, end = " ")

------------

def func_gen(x,y):
    for number in range(x+1):
        yield number ** y
    
for n in func_gen(10,2):
    print(n, end=" ")

   --------------

def decorator(func):
    def wrapper(x):
        print("auth")
        func(1)
    return wrapper

@decorator
def func(x):
    print(f"x = {x}")

func(1)

-------------


def milk(func):
    def wrapper():
        print("hot milk") 
        func()
    return wrapper

def sugar(func):
    def wrapper():
        print("Sugar")
        func()
    return wrapper
@sugar
@milk
def coffee(variety = "arabica"):
    print(variety)

coffee()

----------------

def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def say_whee():
    print("whee!")

say_whee()

@do_twice
def greet(name):
    print(f"hello {name}")
greet("world")


-----------------


def func_fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * func_fact(n-1)
    
print(f"Fatorial of {5} is {func_fact(5)}")


 ------------

glob = 10
def func():
    print(f"global veriable: {glob}")
func()


-------------


glob1 = 10
def func():
    global glob1
    glob1+=1
    print(f"global veriable {glob1}")
func()

--------------

from typing import List

x: int = 1
array = List  = list(range(1,11))
def func(string:str,array:list)->str:
    ssum = 0
    for numb in array:
        ssum += numb
    return f"{string}: {ssum}", 1

lst = [i for i in range(10)]
print(func(f"masivis elementebis jami aris ", lst))
print(type(x))

'''

