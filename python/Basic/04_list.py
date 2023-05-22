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

lst3 = [10, 20, 30, 40, 50, 60, 70, 80]
print(lst3[1:6])  # start 1 step 1
print(lst3[1:6:])  # start 1 step 1
print(lst3[1:6:2])  # start 1 step 2
print(lst3[:6:2])  # start 0 step 2
print(lst3[1::2])  # start 1 step 2

print('original list:', lst3)
print(lst3[::-1])  # start=0, stop=0, step=-1
print(lst3[7::-1])  # start=7, stop=0, step=-1
print(lst3[6:0:-2])  # start=6, stop=0, step=-2

print('p' in 'python')  # true
print(10 in lst3)
print(10 not in lst3)

lst = [10, 20, 30]

for item in lst:
    print(item)
print('id before:', id(lst))
lst.append(40)  # add on the end
print('id after:', id(lst))
lst2 = [40, 50]
lst.extend(lst2)  # add on the end
print(lst)
lst.insert(2, True)
print(lst)
lst3 = [True, False, 'hello']
lst[1:] = lst3
print(lst)

lst = [10, 20, 30, 40, 50, 60]
lst.remove(30)
print(lst)
# lst.remove(100) # error

lst.pop(1)  # pop index
print(lst)
# lst.pop(6)  # error not exist index
lst.pop()  # pop the last one
print(lst)

lst_new = lst[1:3]
print(lst)
print(lst_new)
lst[1:3] = []
print(lst)

lst.clear()
print(lst)

lst = [10, 20, 30, 40, 50, 60]
# del lst
# print(lst)

lst = [10, 20, 30, 40]
lst[2] = 100
print('----------------')
print(lst)
lst[1:3] = [1000, 2000, 3000, 4000]
print(lst)
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)
lst.sort(reverse=False)
print(lst)

lst_new = sorted(lst)
print(lst)
print(lst_new)

