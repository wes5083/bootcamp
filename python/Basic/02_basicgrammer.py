# Comments
print("This is a single comment")
'''
This is multy comments
'''
print("This is multy comments")

# 1: Strings
print("----------------1: Strings-----------------")
print("Giraffe Academy")
print("Giraffe\nAcademy")
print("Giraffe\"Academy")

phrase = "Giraffe Academy"
print(phrase + " is cool.")
print(phrase.lower())  #
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
print(phrase.replace("Gir", "Mar"))

# 2: Numbers
print("----------------2: Numbers-----------------")
print(2 * (3 + 4))
print(10 % 3)
my_num = -5
print(str(my_num) + " my favorite number")
print(abs(my_num))  # 5
print(pow(4, 6))  # 4*4*4*4*4*4 = 4096
print(pow(16, 3))  # 16*16*16 = 4096
print(max(4, 6))  # 6
print(min(4, 6))  # 4
print(round(3.2))  # 3
print(round(3.7))  # 4

from math import *

print(floor(3.7))  # 3
print(ceil(3.7))  # 4
print(sqrt(36))  # 6.0

# 3: Input From User
print("----------------3: Input From User-----------------")
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello " + name + "! You are " + age)

# 4: Lists
print("----------------4: Lists-----------------")
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends2 = ["Kevin", 2, True]
print(friends)  # All
print(friends[0])  # first one
print(friends[-1])  # last one
print(friends[1:])  # from 2 to last one
print(friends[1:3])  # from 2 to 3

friends[1] = "Mike"
print(friends[1])  # Mike

friends.append("Test")  # add at last one
print(friends)

lucky_numbers = [4, 8, 15, 16, 24, 42]
friends.extend(lucky_numbers)  # add two array together
print(friends)
friends.insert(1, "Kelly")  # in the 1 index to add
print(friends)
friends.remove("Jim")  # Jim will be remove
print(friends)
friends.pop()  # remove last one
print(friends)
friends.clear()  # remove all
print(friends)

friends2 = ["Mike", "Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends2.index("Mike"))
print(friends2.count("Karen"))
friends2.sort()
print(friends2)
friends2.reverse()
print(friends2)

friends3 = friends2.copy()
print(friends3)

# 5: Tuples
print("----------------5: Tuples-----------------")
coordinate = (4, 5)
print(coordinate)
print(coordinate[0])  # 4
# coordinate[1] = 10     # not support; can't change
print(coordinate[1])  # 5

coordinates = [(4, 5), (6, 7)]

# 6: Function
print("----------------6: Function-----------------")

# 7: If statement
print("----------------7: If statement-----------------")

# 8: Dictionaries
print("----------------8: Dictionaries-----------------")

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversions["Nov"])
print(monthConversions.get("Luv", "Not a valid Key"))

monthConversions = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

print(monthConversions[3])
print(monthConversions.get(3, "Not a valid Key"))
print(monthConversions.get(13, "Not a valid Key"))

# 9: While loop
print("----------------9: While loop-----------------")

i = 1
while i <= 10:
    print(i)
    i += 1
print("Done with loop")

# 10: While loop
print("----------------10: While loop-----------------")

for letter in "Zhang wes":
    print(letter)

friends = ["Mike", "Jim", "Toby"]
for friend in friends:
    print(friend)

for index in range(10):
    print(index)  # 0 - 9

for index in range(3, 10):
    print(index)  # 3 - 9

for index in range(len(friends)):
    print(friends[index])

# 11: Exponent function
print("----------------11: Exponent function-----------------")

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power(2,3))

# 12: Lists & Nested loop
print("----------------12: Lists & Nested loop-----------------")
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[0][0])    # 1
print(number_grid[2][1])    # 8

for row in number_grid:
    print(row)
    for col in row:
        print(col)


# 13: Try/Expect
print("----------------13: Try/Expect-----------------")

try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print("Divided by Zero")
    print(err)
except ValueError:
    print("Invalid Input")




