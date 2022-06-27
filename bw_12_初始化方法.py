"""
作者：Ben Wang
时间：2022/6/25
"""


class Cat:
    """这是一个猫类"""

    def __init__(self, name):
        # print("这是一个初始化方法！")

        # self.属性名 = 属性的初始值
        # tom = Cat("Tom")
        # 在方法内部，使用self.属性 = 形参 接收外部传递的参数
        self.name = name

    def eat(self):
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("%s 爱喝水" % self.name)


# 使用类名()创建对象的时候，会自动调用初始化方法 __init__
tom = Cat("Tom")
tom.eat()
lazy_cat = Cat("Lazy_cat")
lazy_cat.drink()

