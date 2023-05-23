t = ('Hello', 'World', 'Python')
print(t, type(t))
t = ('Hello',)
print('-----only one element-----', t, type(t))
t = ('Hello')
print('-----only one element-----', t, type(t))

t = tuple(('Hello', 'World', 'Python'))
print(t, type(t))
t = 'Hello', 'World', 'Python'
print(t, type(t))

print(t[0])
print(t[1])
print(t[2])

for item in t:
    print(item)

lst = []
lst1 = list()
print(type(lst), type(lst1))
d = {}
d1 = dict()
print(type(d), type(d1))
t = ()
t1 = tuple()
print(type(t), type(t1))

lst = [10, 20, 30]
print(id(str))
lst.append(100)
print(id(str))

s = 'hello'
print(id(s))
s = s + ' world'
print(id(s))
