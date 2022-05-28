# 定义函数是，是否接收参数，或者是否返回结果，是根据实际的功能需求来决定的
# 1.如果函数内部处理的数据不确定，就可以将外界的数据以参数传递到函数内部
# 2.如果希望一个函数执行完成后，向外界汇报执行结果，就可以增加函数的返回值
def measure():

    print("测量开始...")
    temp = 39
    wetness = 50
    print("测量结束...")

    return temp, wetness
    # 如果函数返回的类型是元祖，小括号可以省略


# result = measure()
# print(result)
#
# # 需要单独的处理温度或湿度
# print(result[0])
# print(result[1])

# 使用多个变量接收函数返回的结果
gl_temp, gl_wetness = measure()
print(gl_temp)
print(gl_wetness)
