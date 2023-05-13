# If statement & Comparisons
print("----------------If statement & Comparisons-----------------")

is_male = True
is_tale = False

if is_male:
    print("You are a male.")
else:
    print("You are not a male.")

if is_male or is_tale:
    print("You are a male or tall or both.")
else:
    print("You neither male nor tall.")

if is_male and is_tale:
    print("You are a tall male.")
elif is_male and not (is_tale):
    print("You are a short male.")
elif not (is_male) and is_tale:
    print("You are not a male but are tall.")
else:
    print("You are not a male and not tall.")


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


result = max_num(1, 5, 9)
print(result)

print("----------------Building a Better Calculator-----------------")

num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter first number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalidate operate!")
