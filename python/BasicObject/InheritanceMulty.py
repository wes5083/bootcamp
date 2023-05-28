class A(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'My name is {0}'.format(self.name)


class B(object):
    pass


class C(A, B):
    pass


# object default is all the class's father
a = A('zhangsan')
print(dir(a))
print(a)
print(type(a))