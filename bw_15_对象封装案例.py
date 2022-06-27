"""
作者：Ben Wang
时间：2022/6/25
"""
"""
需求：
1、小明体重75.0公斤
2、小明每次跑步减肥0.5公斤
3、小明每次迟东西，体重增加1公斤
"""


class Person:

    def __init__(self, name, weight):

        # self.属性 = 形参
        self.name = name
        self.weight = weight

    def __str__(self):

        return "我是【%s】，体重是%.1f" % (self.name, self.weight)

    def run(self):
        print("%s爱跑步，跑步锻炼身体" % self.name)

        self.weight -= 0.5

    def eat(self):
        print("%s是吃货，吃完这顿再减肥" % self.name)

        self.weight += 1


xiaoming = Person("小明", 75.0)

xiaoming.run()
xiaoming.eat()

print(xiaoming)


xiaomei = Person("小美", 45.0)

xiaomei.run()
xiaomei.eat()

print(xiaomei)
