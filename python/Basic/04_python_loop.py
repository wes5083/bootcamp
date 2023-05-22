# rang

r = range(10)
print(r)  # rang(0,10)
print(list(r))  # [1...9]

r = range(1, 10)
print(list(r))  # [1...9]

r = range(1, 10, 2)
print(list(r))  # [1,3,5,7,9]

for i in range(1, 4):
    for j in range(1, 5):
        print('*', end='\t')
    print()

for i in range(1, 10):
    for j in range(1, i + 1):
        print(i, '*', j, '=', i * j, '  ', end='')
    print()

# in, not in
print(10 in r)
print(9 in r)
print(10 not in r)
print(9 not in r)

# while loop / for in
a = 1
while a < 10:
    print(a)
    a += 1

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][0])  # 1
print(number_grid[2][1])  # 8

for row in number_grid:
    print(row)
    for col in row:
        print(col)

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




