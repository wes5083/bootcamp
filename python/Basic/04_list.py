a = 10
lst = ['hello', 'world', 98, 'hello']
print(id(lst))
print(type(lst))
print(lst)
lst2 = list(['hello', 'world', 98, 'hello'])
print(id(lst2))
print(type(lst2))
print(lst2)

print(lst.index('hello'))
print(lst.index('hello', 1, 4))
print(lst[1], lst[-1])

lst3 = [10, 20, 30, 40, 5, 60]
print(lst3[1:6])  # start 1 every 1
print(lst3[1:6:])  # start 1 every 1
print(lst3[1:6:2])  # start 1 every 2
print(lst3[:6:2])  # start 0 every 2
