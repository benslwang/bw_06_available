"""
作者：Ben Wang
时间：2022/6/25
"""


class Cat:

    def eat(self):
        # 哪一个对象调用的方法，self就是哪一个对象的引用
        print("%s爱吃鱼" % self.name)

    def drink(self):
        print("%s爱喝水" % self.name)


tom = Cat()

# 可以使用 .属性名   利用赋值语句就可以了
tom.name = "Tom"

tom.eat()
tom.drink()
"""
当使用类名()创建对象时，会自动执行以下操作：
1、为对象在内存中分配空间——创建对象
2、为对象的属性设置初始值——初始化方法（init）
这个初始化方法就是__init__方法，是对象的内置方法
"""