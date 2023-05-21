# rang

r = range(10)
print(r)  # rang(0,10)
print(list(r))  # [1...9]

r = range(1, 10)
print(list(r))  # [1...9]

r = range(1, 10, 2)
print(list(r))  # [1,3,5,7,9]

# in, not in
print(10 in r)
print(9 in r)
print(10 not in r)
print(9 not in r)
