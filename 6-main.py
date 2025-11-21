
'''
class myClass:
    def __init__(self):
        self.x = 10
    def info(self):
        print(f"get value of attribute using method: {self.x}")
c = myClass()
c.info()
print(f"get value of attribute using object: {c.x}")
print(myClass.__doc__)

-------------



class myClass:
    attr_cl = 10
    def __init__(self):
        self.attr_x = 15

c = myClass()
print('object attrribute: ')
print(f"before: c.attr_x: {c.attr_x}")

c.attr_x = 50
print(f"after: {c.attr_x}")

a = myClass()
b = myClass()

print(f"obj a attr_cl = {a.attr_cl}")
print(f"obj b attr_cl = {b.attr_cl}")
print('class atrribute:')

print(f'Before: myclass.attr_cl = {myClass.attr_cl}')
myClass.attr_cl = 20
print(f'obj a attr_cl = {a.attr_cl}')
print(f'obj b attr_cl = {b.attr_cl}')

print(f'after: myClass.attr_cl = {myClass.attr_cl}')


-------------

'''


class myClass:
    pass
myClass.attr_d = 50

c1,c2 = myClass(), myClass()
c1.attr_d = 30

print(f'Object level dynamic attribute: c1.attribute_d = ', c1.attr_d)
print('Class level dynamic attribute: c2.attr_d = ', c2.attr_d)
