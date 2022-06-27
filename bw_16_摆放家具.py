"""
作者：Ben Wang
时间：2022/6/25
"""

"""
摆放家具
1、房子House有户型、面积和家具名称列表
    新房子没有任何家具
2、家具HouseItem有名字和占地面积，其中：
    席梦思bed占地4平米
    衣柜chest占地3平米
    餐桌table占地1.5平米
3、将以上3件家具添加到房子中
4、打印房子时，要求输出：户型、总面积、剩余面积、家具名称列表
"""


class HouseItem:

    def __init__(self, name, area):

        # self.属性 = 形参
        self.name = name
        self.area = area

    def __str__(self):

        return "【%s】占地%.1f平米" % (self.name, self.area)


class House:

    def __init__(self, house_type, area):

        self.house_type = house_type
        self.area = area

        # 剩余面积
        self.free_area = area

        # 家具名称列表
        self.item_list = []

    def __str__(self):

        # python能够自动将一对括号内的代码间接在一起
        return ("户型：%s\n总面积：%.2f[剩余：%.2f]\n家具：%s"
                % (self.house_type, self.area,
                   self.free_area, self.item_list))

    def add_item(self, item):

        print("要添加%s" % item)


# 创建家具
bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 3)
table = HouseItem("餐桌", 1.5)

print(bed)
print(chest)
print(table)


# 创建房子对象
my_home = House("两室一厅", 60)

print(my_home)
