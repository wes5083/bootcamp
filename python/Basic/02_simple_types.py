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


print("---------3: Str---------")
str1 = "This is str"  # only one  line
str2 = 'This is str'  # only one  line
str3 = """This is 
str"""  # Can be multiline
str4 = '''This is 
str'''  # Can be multiline

print(str1, type(str1))  # This is str  str
print(str2, type(str2))
print(str3, type(str3))
print(str4, type(str4))

print("---------4: Data type conversion---------")

name = "Wes"
age = 10
print(name + " age is " + str(age))  # Wes age is 10
'''
str()
inf()   
float()
'''

print(str(123))         # 123
print('123')            # 123
print(int('123'))       # 123 -> int
print(int(9.8))         # 9     round off
print(float('9.8'))     # 9.8
print(float(9.8))       # 9.8

b3 = True
print(str(b3), type(str(b3)))       # True, str
print(int(b3), type(int(b3)))       # 1, int
print(float(b3), type(float(b3)))   # 1.0, float

# string word or with decimal cannot be converted to int
# string word cannot be converted to float
try:
    print(int('name'))
    print(int('9.99'))
    print(float('name'))
except ValueError:
    print("string word cannot be converted to int and float")
    print("string with decimal point cannot be converted to int and float")