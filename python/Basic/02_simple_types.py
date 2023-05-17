'''
simple types
int
float
Decimal
bool
str

'''

print("---------1: Numbers---------")
n1 = 90
n2 = -7
n3 = 1.1
n4 = 2.1
n5 = 2.2
print(n1, type(n1))  # 90 int
print(n2, type(n2))  # -7 int
print(n3, type(n3))  # 1.1 float

print(n3 + n4)  # 3.2
print(n3 + n5)  # sometimes overflow    3.3000000000000003
from decimal import Decimal

print(Decimal('1.1') + Decimal('2.2'))  # Accurate calculation need Decimal 3.3

print('default is decimal: ', 18)  # 18
print('binary: ', 0b111)  # start 0b      7
print('Octal: ', 0o777)  # start 0o      511
print('hexadecimal: ', 0xFFF)  # start 0x      4095


print("---------2: Boolean---------")

b1 = True  # can be converted to an integer 1
b2 = False  # can be converted to an integer 0
print(b1, type(b1))  # True bool
print(b2, type(b2))  # False bool
print(b1 + 1.1)  # 2.1
print(b2 + 1)  # 1
