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
