# 定义函数时，可以给某个参数制定一个默认值，具有默认值的参数就叫做缺省参数
# 调用函数时，如果没有传入缺省参数的值，则在函数内部使用定义函数时指定的参数默认值
# 函数的缺省参数，将常见的值设置为函数的缺省值（默认值），从而简化函数的调用
gl_list = [6, 3, 9]

# 默认按照升序排序
gl_list.sort()
print(gl_list)

# 如果需要降序排序，需要指定reverse参数
gl_list.sort(reverse=True)
print(gl_list)


def print_info(name, gender=True):
    """

    :param name: 班上同学的姓名
    :param gender: True 男生 False 女生
    """

    gender_text = "男生"

    if not gender:
        gender_text = "女生"

    print("%s 是 %s" % (name, gender_text))


# 提示：在指定缺省函数的默认值时，应该使用最常见的值作为默认值（缺省值）！
print_info("小明")
print_info("小美", False)

"""
必须保证带有默认值的缺省参数在函数列表末尾
"""
