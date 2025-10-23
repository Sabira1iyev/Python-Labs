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

'''

def user_func(*, a,b, c=10):
    return a+ b+c
c = user_func(1,2,1)
#c = user_func(a = 1, b=5)
print(c)