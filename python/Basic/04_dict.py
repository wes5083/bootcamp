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

'''
dictionary = {key: expression for (key, value) in iterable}
dictionary = {key: expression for (key, value) in iterable if conditional}
dictionary = {key: (if/else) for (key, value) in iterable}
dictionary = {key: function(value) for (key, value) in iterable}
'''
weather_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
weather_in_C = {key: round((value - 32) * (5 / 9)) for (key, value) in weather_in_F.items()}
print(weather_in_C)
weather = {'New York': 'snowing', 'Boston': 'sunny', 'Los Angeles': 'sunny', 'Chicago': 'cloudy'}
weather_sunny = {key: value for (key, value) in weather.items() if value == "sunny"}
print(weather_sunny)
weather_desc = {key: ("WARM" if value >= 40 else "COLD") for (key, value) in weather_in_F.items()}
print(weather_desc)


def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 69 >= value >= 40:
        return "WARM"
    else:
        return "CODE"

weather_function = {key: check_temp(value) for (key, value) in weather_in_F.items()}
print(weather_function)
