scores = {'zhangsan': 1001, 'zhangsan': 100, 'lisi': 98, 'wangwu': 45}
print(scores['zhangsan'])
print(scores.get('zhangsan'))
# print(scores['zhangsan1']) # KeyError
print(scores.get('zhangsan1'))  # None
# del scores['zhangsan']
# scores.clear()  # clear dict
scores['chenliu'] = 88  # add

keys = scores.keys()
print(keys)
print(type(keys))
print(list(keys))

values = scores.values()
print(values)
print(type(values))
print(list(values))

items = scores.items()
print(items)
print(type(items))
print(list(items))  # tupe

for item in scores:
    print(item, scores[item], scores.get(item))

item = ['fruits', 'books', 'others']
prices = [96, 78, 85]
d = {item: price for item, price in zip(items, prices)}
print(d)
