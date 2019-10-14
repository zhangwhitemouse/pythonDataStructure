# 问题描述：进制转换
"""
算法分析：
    我们正常使用的语言是十进制的，但是计算机使用的是二进制的。
    从十进制转换成二进制就是不停的除2，我们可以使用栈来跟踪每次除2的余数
    最后再将栈中的数再pop出来，构成二进制序列。栈底元素（第一个元素）相当于序列的最后一个元素
解决方案：
    从简单的二进制转换出发，拓展到多进制的转换
"""

from python_stack import Stack

def binary_Conversion(decNumber):
    "将十进制数转换成二进制"

    s = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        s.push(rem)
        decNumber = decNumber // 2

    "拼接字符串"
    string = ""
    while not s.isEmpty():
        string = string + str(s.pop())

    return string

print(binary_Conversion(20))


"""
问题拓展：
    可以将十进制的数转换成任意进制数
解决方案：
    考虑转换成哪个进制，需要多传一个参数。
    转换成哪个进制，就除几
"""

def binary_Conversion(decNumber,base):
    "将十进制数转换成任意进制"

    s = Stack()

    while decNumber > 0:
        rem = decNumber % base 
        s.push(rem)
        decNumber = decNumber // base 

    "拼接字符串"
    string = ""
    while not s.isEmpty():
        string = string + str(s.pop())

    return string

print(binary_Conversion(20,8))

"""
当然问题还可以拓展为任意进制数转换成任意进制
这个时候，需要将原来的数先转换成10进制数，然后再转换成目标进制
"""