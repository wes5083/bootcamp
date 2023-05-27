# String formate
name = 'zhangsan'
age = 30
# 1. %
print('My name is %s, my age is %d years old' % (name, age))
# 2. {}
print('My name is {0}, my age is {1} years old'.format(name, age))
# 3. f-string
print(f'My name is {name}, my age is {age} years old')
# 4. decimal formate
print('%d' % 99)
print('%10d' % 99)  # width
print('%f' % 3.1415926)
print('%10.3f' % 3.1415926)  # width & precision
print('{0}'.format(3.1415926))
print('{0:.3}'.format(3.1415926))  # all together is 3 numbers
print('{0:.3f}'.format(3.1415926))
print('all together is 10:  {:10.3f}'.format(3.1415926))

# string code&encode
s = '测试-test'
byte = s.encode(encoding='UTF-8')
print(byte.decode(encoding='UTF-8'))
byte = s.encode(encoding='GBK')  # encode
print(byte.decode(encoding='GBK'))  # decode
