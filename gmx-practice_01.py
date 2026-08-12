# coding=utf-8

"""
2026-07-26 20:44
"""

# Practice 1

"""
a = 13
b = 6

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")

# print语句也可以写成如下形式
print(a,"+",b,"=",a + b)
"""

# Practice 2

"""
x = 13
y = 12.5
z = "Welcome"

x_int = isinstance(x, int)
y_int = isinstance(y, int)
z_int = isinstance(z, int)

print(f"变量x的类型是否为int: {x_int}")
print(f"变量y的类型是否为int: {y_int}")
print(f"变量z的类型是否为int: {z_int}")
"""

# Practice 3

"""
input_1 = input("number1:")
input_2 = input("number2:")

int_1 = int(input_1)
int_2 = int(input_2)

int_3 = int_1 + int_2

print(f"{int_1} + {int_2} = {int_3}")
"""

# Practice 3  --another version

"""
input_1 = int(input("number1:"))
input_2 = int(input("number2:"))

print(f"{input_1} + {input_2} = {input_1 + input_2}")
"""

# Practice 4

"""
ht = int(input("您的身高(cm)为:")) / 100  # 这里用ht简称height
wt = float(input("您的体重(kg)为:"))  # 这里用wt简称weight

bmi = wt / (ht ** 2)

print(f"您的BMI指数为: {bmi}")
"""

# Practice 5

"""
ht = int(input("您的身高(cm)为:")) / 100  # 这里用ht简称height
wt = float(input("您的体重(kg)为:"))  # 这里用wt简称weight

bmi = wt / (ht ** 2)

print(f"\n您的BMI指数为: {bmi}")
"""

# a = 0.3
# b = 0.4
# c = a + b
#
# import random
# import time
#
# print(3 / 0.1)
# print(random.random.path)
# time.sleep(10)

# while 1:
#     pass

# a = range(10)
# print(a)

# s = [11,22,33,44,55,66,77,88]
# print(s[:7:2])

# for i in range(10):
#     print(i, end = "")

# 梯形面积计算

"""
a = int(input("up="))
b = int(input("dn="))
h = int(input("ht="))

squ = (a + b) * h / 2

print(f"square = {squ}")
"""

# 字符串加法

"""
a = "He"
b = "llo"
print(a + b)
"""

# 整除

"""
a = 7
b = -2
c = a // b
print(c)
"""

# 布尔值0即False, 1即True

"""
a = 0
a = bool(a)
print(a)
"""

# print的sep参数
"""
print("he","llo","you",sep = "",end = "")
print(111)
"""

# for循环实现100以内奇数求和
"""
num = 0
for i in range(1,101,2):
    num = num + i
print(num)
"""

# 九九乘法表
"""
for hang in range(1,10):
    for lie in range(1,hang+1):
        ji = lie * hang
        wei = len(str(ji))
        print(f"{lie} * {hang} = {ji}{(4-wei)*" "}", end = "")
    print()
"""

