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

