# 有两个整数变量 a = 6, b = 100
# 不使用其他变量，交换两个变量的值
a = 6
b = 100

# # 1.使用其他变量
# c = a
# a = b
# b = c
# print(a)
# print(b)

# # 2.不使用其他变量
# a = a + b
# a = a - b
# b = a - b

# 3.python专用
a, b = (b, a)  # ()可省略


print(a)
print(b)
