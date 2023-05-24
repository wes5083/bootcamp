s1 = 'aaa'
s2 = 'aaa'
print(s1 is s2)

s = 'hello, hello, python'
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
