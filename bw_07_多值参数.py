"""
有时可能需要一个函数能够处理的参数个数是不确定的，这个时候，就可以使用多值参数。

python中有两种多值参数
    参数名前增加一个*，可以接收元祖
    参数名前增加两个*，可以接收字典
一般给多值参数命名时，习惯使用以下两个名字
    *args 存放元祖参数
    **kwargs 存放字典参数
    （args是argument的缩写，有变量的意思，kwargs可以记忆键值对参数）
"""


def demo(num, *nums, **person):
    print(num)
    print(nums)
    print(person)


# demo(1)
demo(1, 2, 3, 4, 5, name="小明", age=18)


def sum_numbers(*args):
    num = 0

    print(args)
    # 遍历循环
    for n in args:
        num += n

    return num


result = sum_numbers(1, 2, 3, 4)
print(result)
