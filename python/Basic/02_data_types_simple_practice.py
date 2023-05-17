print("---------Data type conversion---------")

s1 = '128'
s2 = '128.99'
s3 = 'hello'
f1 = 98.77
f2 = 98
b1 = True

print("--------int(): str -> int, it must be an integer number--------")
print(int(s1), type(int(s1)))       # 128
# print(int(s2), type(int(s2)))     #
# print(int(s3), type(int(s3)))     #
print(int(f1), type(int(f1)))       # 98  round off  from 98.77 to 98
print(int(f2), type(int(f2)))       # 98
print(int(b1), type(int(b1)))       # 1

print("--------float(): str -> float, it must be an number--------")
print(float(s1), type(float(s1)))       # 128.0
print(float(s2), type(float(s2)))       # 128.99
# print(float(s3), type(float(s3)))     # can't convert a word to float
print(float(f1), type(float(f1)))       # 98.7
print(float(f2), type(float(f2)))       # 98.0
print(float(b1), type(float(b1)))       # 1.0