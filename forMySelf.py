from abc import ABC, abstractmethod
from zipfile import ZipFile

# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass

# class Cat(Animal):
#     def sound(self):
#         print("Miyav")

# class Dog(Animal):
#     def sound(self):
#         print("Hav Hav")

# c1 = Cat()
# print(c1.sound())

# class Car:
#     def drive(self):
#         print("worked")
#     def inf():
#         print("this is a car class")

# a = Car()
# print(a.drive())
# Car.inf()

# class Record:
#     def __init__(self,region, year):
#         self.region = region
#         self.year = year

# records = [Record("Germany", 2020), Record("USA", 2020)]
# filters = {"region", "Germany"}

# result = []

# for rec in records:
#     match = True
#     for key, value in filters.items():
#         if hasattr(rec,key):
#             attr = getattr(rec,key)
#             if attr != value:
#                 match = False
#                 break 
#         else:
#             match = False
#             break
#     if match:
#         result.append(rec)

# print(len(result))


# x = 5

# print(isinstance(x,int))
# print(isinstance(x,float))

# y = [1,2,3]

# print(isinstance(y,list))
# print(isinstance(y,tuple))

# z = (2012, 2015)
# print(isinstance(z,tuple))
# print(isinstance(z,list))



# class Car:
#     def normal_method(self):
#         print("this is normal meethod: ", self)
    
#     @staticmethod
#     def static_method():
#         print("this is static method, self doesnt come automatically!")


# a = Car()

# a.normal_method()
# print(a)

# print(a.static_method())



# with ZipFile("cars.zip", "r") as z:
#     print(z.namelist())

# with z.open("file1.txt") as f:
#     for line in f:
#         print(line.decode('utf-8').strip())

