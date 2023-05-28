class A:
    def __new__(cls, *args, **kwargs):
        print('__new__ was be called id={0}'.format(id(cls)))
        obj = super().__new__(cls)
        print(' new object id={0}'.format(id(obj)))
        return obj

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('__init__ was be called. self id={0}'.format(id(self)))


class B:
    pass


class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other):
        return self.name + ' ' + other.name


print('------spacial attribute-----')
x = C('Jack', 20)
print(x.__dict__)  # instance attribute
print(C.__dict__)
print(x.__class__)  # <class '__main__.C'>
print(C.__bases__)  # father class: (<class '__main__.A'>, <class '__main__.B'>)
print(C.__base__)  # the first father: <class '__main__.A'>
print(C.__mro__)  # class's layer construct
print(A.__subclasses__())  # sub classes

print('------__add__ method -----')
a = 20
b = 100
c = a + b
d = a.__add__(b)

c1 = C('zhangsan', 20)
c2 = C('lisi', 20)
c3 = c1 + c2
print(c3)  # object implement __add__ method

print('------__len__ method -----')
lst = [11, 22, 33, 44]
print(len(lst))
print(lst.__len__())
print(len(c3))

print('------__new__ method -----')

print('object class id={0}'.format(id(object)))
print('A class id={0}'.format(id(A)))
a = A('zhangsan', 20)
print('A class instance object id={0}'.format(id(a)))
