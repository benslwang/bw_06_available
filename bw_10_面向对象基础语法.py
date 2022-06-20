"""
dir 内置函数
    使用内置函数dir传入标识符/数据，可以查看对象内的所有属性与方法
"""


def demo():
    """这是一个测试函数"""
    print("hello python")


demo()
print(demo.__doc__)
print(demo.__module__)

"""
定义只包含方法的类
    在python中要定义一个只包含方法的类，语法格式如下：
class 类名:
    def 方法1(self, 参数列表):
        pass
    def 方法2(self, 参数列表):
        pass

创建对象
    当一个类定义完成后，要使用这类来创建对象，语法格式如下：
变量对象 = 类名()
"""


class Cat:

    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")


# 创建猫对象
tom = Cat()

tom.eat()
tom.drink()

print(tom)

# 内存地址
addr = id(tom)
# 十进制
print("%d" % addr)
# 十六进制
print("%x" % addr)

# 再创建一个猫对象
lazy_cat = Cat()

lazy_cat.eat()
lazy_cat.drink()

print(lazy_cat)
