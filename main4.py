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


'''

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
