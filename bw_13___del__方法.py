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


tom = Cat("Tom")

