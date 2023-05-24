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

s = {10, 20, 30}
print(10 in s)
print(100 in s)
print(10 not in s)
print(100 not in s)

''' collection ADD '''
s.add(80)
print(s)
s.update({100, 200})
print(s)
s.update([300, 400])
print(s)
s.update((500, 600))
print(s)

'''collection delete'''

s.remove(100)
print(s)
s.remove(500)
print(s)

s.discard(500)
s.discard(300)
print(s)
s.pop()
s.pop()
# s.pop(999)
print(s)

s1 = {10, 20, 30}
s2 = {10, 30, 20}
s3 = {10, 20}
s4 = {10, 20, 30, 40, 50}
print(s1 == s2)
print(s1 != s2)

print(s3.issubset(s2))
print(s4.issuperset(s3))

print(s2.isdisjoint(s3))
s5 = {100, 200}
print(s2.isdisjoint(s5))

print(s1 & s2)
print(s1.union(s2))
print(s1 | s2)

print(s1.difference(s2))

