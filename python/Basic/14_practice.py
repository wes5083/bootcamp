data = []
for i in range(10):
    data.append(i)
print(data)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

data = [i for i in range(10)]
print(data)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

data = [i for i in range(10) if i < 5]
print(data)  # [0, 1, 2, 3, 4]
