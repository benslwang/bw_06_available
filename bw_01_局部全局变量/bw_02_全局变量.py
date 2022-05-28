# 全局变量
num = 10
# print(num)

def demo1():

    # 希望修改全局变量的值- 使用global声明一下变量即可
    global num
    # global关键字会告诉解释器后面的变量是一个全局变量
    # 再使用赋值语句时，就不会创建局部变量
    # 在Python中，是不允许直接修改全局变量的值
    # 如果使用赋值语句，会在函数内部使用一个局部变量
    num = 99

    print("demo1==> %d" % num)
    print("%s" % num2)


num2 = 9999

def demo2():

    print("demo2==> %d" % num)


demo2()
print(num)
demo1()
# demo2()
print(num)

# 全局变量是在函数外部定义的变量（没有定义在某个函数内），所有函数内部都可以使用这个变量
# shebang==>import模块==>全局变量==>函数定义==>执行代码
