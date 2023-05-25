s1 = 'aaa'
s2 = 'aaa'
print(s1 is s2)

s = 'hello, python'
print(s.index('lo'))
print(s.find('lo'))
print(s.rindex('lo'))
print(s.rfind('lo'))

print(s.find('k'))
# print(s.rindex('k')) # ValueError: substring not found
print(s.rfind('k'))

s2 = s.upper()
print(s, id(s))
print(s2, id(s2))
print(s.lower(), id(s.lower()))
print(s, id(s.lower()))
s3 = s.lower()  # new string object

print(s3, id(s3))
print(s, id(s))
print(s3 == s)
print(s3 is s)

print(s2.swapcase())
print(s2.center(20, '*'))
print(s.ljust(20, '*'))
print(s.ljust(10))
print(s.ljust(10))
print(s.rjust(20, '*'))
print(s.rjust(20))
print(s.zfill(20))
print(s.zfill(10))
print('-8910'.zfill(8))
print(s2.title())

s = 'hello world python'
lst = s.split()  # default is  space
print(lst)
s = 'hello|world|python'
print(s.split(sep='|'))  # start left
print(s.split(sep='|', maxsplit=1))
print(s.rsplit('|'))
print(s.rsplit(sep='|', maxsplit=1))

print('1.', s.isidentifier())  # False
print('2.', 'hello'.isidentifier())  # True
print('3.', 'zhangsan_'.isidentifier())  # True
print('4.', '\t'.isspace())  # True
print('5.', 'abc'.isalpha())  # True
print('6.', 'zhangsan'.isalpha())  # True
print('7.', 'zhangsan1'.isalpha())  # False
print('8.', '123'.isdecimal())  # True
print('9.', '123zhang'.isdecimal())  # False
print('10.', '123'.isnumeric())  # True
print('11.', '123zhang'.isnumeric())  # True

print('12.', 'abc1'.isalnum())  # True
print('13.', 'zhangsna123'.isalnum())  # True
print('14.', 'abc!'.isnumeric())  # False

s = 'Hello Python, Hello Python,Hello Python'
print(s.replace('Python', 'Java'))
print(s.replace('Python', 'Java', 2))

lst = ['Hello', 'java', 'python']
print('|'.join(lst))
print(''.join(lst))

lst = ('Hello', 'java', 'python')
print('|'.join(lst))
print('*'.join('Python'))













