"""
一个函数的内部，自己调用自己
    函数内部可以调用其他的函数，也可以调用自己

"""
def sum_number(num):

    print(num)
    # 递归的出口，当参数满足某个条件时，不再执行函数
    if num == 1:
        return

    # 自己调用自己
    sum_number(num - 1)


sum_number(3)


# 递归案例————计算数字累加
def sum_numbers(num):

    # 指定出口
    if num == 1:
        return 1

    # 数字的累加 num + (1 + ... + num-1)
    # 设置一个变量
    temp = sum_numbers(num - 1)
    return num + temp


result = sum_numbers(6)
print(result)

# 递归是一个编程技巧，在处理不确定的循环条件时，非常有用。例如：遍历整个文件目录的结构
