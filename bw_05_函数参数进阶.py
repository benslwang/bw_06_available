def demo(num, num_list):

    print("函数内部的代码")

    # 在函数内部，针对函数使用赋值语句时，不会修改外部的实参变量
    num = 100
    num_list = [1, 2, 3]

    print(num)
    print(num_list)
    print("函数执行完成")


gl_num = 99
gl_list = [4, 5, 6]
demo(gl_num, gl_list)
print(gl_num)
print(gl_list)


def demo1(num_list1):

    print("函数内部的代码")

    # num_list1 = [11, 12, 13]
    # 使用方法修改列表内容
    num_list1.append(10)

    print(num_list1)

    print("函数执行完成")


gl_list1 = [7, 8, 9]
demo1(gl_list1)
print(gl_list1)


def demo2(num, num_list):

    print("函数开始")
    num += num
    # 列表变量使用+=，不会做相加再赋值的操作，本质上是调用列表的extend方法
    num_list += num_list  # 即 num_list.extend(num_list)
    """
    列表变量使用+，不会修改全局变量的结果
    num_list = num_list + num_list
    """
    print(num)
    print(num_list)
    print("函数完成")


gl_num = 9
gl_num_list = [11, 12, 13]
demo2(gl_num, gl_num_list)
print(gl_num)
print(gl_num_list)
