s1 = {2, 3, 4, 5, 2, 3}  # not allow repeat
print(s1)

s2 = set(range(6))
print(s2, type(s2))

s3 = set([2, 3, 4, 5, 2, 3])
print(s3, type(s3))

s4 = set((2, 3, 4, 5, 2, 3))
print(s4, type(s4))

s4 = set('python')
print(s4, type(s4))

s4 = set({2, 3, 4, 5, 2, 3})
print(s4, type(s4))

lst = []
lst1 = list()
print(type(lst), type(lst1))
d = {}
d1 = dict()
print(type(d), type(d1))
t = ()
t1 = tuple()
print(type(t), type(t1))
s = set()
print(type(s))
