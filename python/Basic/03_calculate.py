print(1 + 1)
print(1 - 1)
print(1 * 2)
print(11 / 2)  # 5.5
print(11 // 2)  # 5 get int
print(11 % 2)  # 1
print(2 ** 3)  # 2*2*2=8

print(9 // 4)  # 2
print(-9 // -4)  # 2
# get integer down
print(9 // -4)  # -3
print(-9 // 4)  # -3

# remainder = dividend - divisor * quotient
print(9 % -4)  # -3    9-(-4)*(-3) = -3
print(-9 % 4)  # 3     -9-(4)*(-3) = 3

a = b = c = 20  # assignment
print(a, id(a))
print(b, id(b))
print(c, id(c))

a, b, c = 20, 30, 40
print(a, id(a))
print(b, id(b))
print(c, id(c))

a += 10
print(a)

a -= 10
print(a)

a *= 10
print(a)

a /= 10
print(a)

a = 10
b = 10
print(a == b)
print(a >= b)
print(a <= b)
print(a != b)
print(a is b)  # True: a equal b and a.id equal b.id
print(a is not b)  # False

list1 = [11, 22, 33, 44]
list2 = [11, 22, 33, 44]
print(list1 is list2)  # False
print(id(list1))
print(id(list2))
print(list1 is not list2)  # True

print(4 & 8)  # all is 1 the result is 1
print(4 | 8)  # all is 0 the result is 0

# Move one bit to the left, equivalent to multiplying by 2
print(4 << 1)  # 8
print(4 << 2)  # 16
# Move one bit to the right, equivalent to divided by 2
print(4 >> 1)  # 2
print(4 >> 2)  # 1


'''
#
1. **
2. *,/,//,%       
3. +，-
4. <<, >>
5. &
6. |
7. >,<,==,!=, >=, <=
8. and
9. or
10. =

'''

