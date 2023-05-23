scores = {'zhangsan': 100, 'lisi': 98, 'wangwu': 45}
print(scores['zhangsan'])
print(scores.get('zhangsan'))
# print(scores['zhangsan1']) # KeyError
print(scores.get('zhangsan1'))  # None
del scores['zhangsan']
scores.clear()  # clear dict
scores['chenliu'] = 88  # add
