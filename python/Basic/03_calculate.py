
print(1+1)
print(1-1)
print(1*2)
print(11/2)     # 5.5
print(11//2)    # 5 get int
print(11%2)     # 1
print(2**3)     # 2*2*2=8


print(9//4)     # 2
print(-9//-4)   # 2
# get integer down
print(9//-4)    # -3
print(-9//4)    # -3

# remainder = dividend - divisor * quotient
print(9%-4)     # -3    9-(-4)*(-3) = -3
print(-9%4)     # 3     -9-(4)*(-3) = 3


# Basic calculate
print("----------------Basic calculate-----------------")

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

result = num1 + num2
print(result)  # string add

# only support int, other function float and so on
result = int(num1) + int(num2)
print(result)  # number add
