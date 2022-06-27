"""
作者：Ben Wang
时间：2022/6/25
"""


class Cat:

    def __init__(self, name):

        self.name = name

        print("%s来了" % self.name)

    def __del__(self):
        print("%s去了" % self.name)

    def __str__(self):
        # 在开发中，希望使用print输出对象变量时，能够打印自定义的内容，可以使用__str__这个内置方法
        # __str__方法必须返回一个字符串
        return "我是小猫【%s】" % self.name


tom = Cat("Tom")
print(tom)
