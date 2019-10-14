#问题:判断括号是否匹配
"""
算法分析:
    从简单的单一括号匹配开始,跳出思维误区,不能简单的从数量上进行判断,
    还要考虑左右括号是否匹配
解决方案:
    1 遇到左括号就把它压入栈
    2 遇到第一个右括号的时候,将栈中栈顶的左括号弹出,形成一对
    3 依次遍历字符串,直到结束的之后,看栈中是否还有括号
    4 有,括号不匹配;没有,说明匹配
"""
from python_stack import Stack

def bracket_matching(character):
    "单一符号匹配"

    balance = True
    s = Stack()

    for i in character:
        #print(i)
        if i == '(':
             s.push(i)
        if i == ')':
            if s.isEmpty():
                balance = False
                break
            else:
                s.pop()

    if not s.isEmpty():
        balance = False

    return balance


print(bracket_matching("(((()))"))


"""
多类型括号的匹配问题:
    包括[],{},()的混合判断

解决方案:
    大体思想和单一括号匹配是差不多的,
    但是如果依次进行左括号的判断的话,代码太繁琐
    所以我们将所有的左括号放入一个列表中
    其次,多类型括号的判断,要多一个判断条件,
    因为必须保证括号的类型一致,避免出现 (} [)这些情况
"""

def brackets_matching(character):
    "多类型括号匹配"

    s = Stack()
    balance = True

    symbol = ['(','[','{']

    for i in character:
        if i in symbol:
            #print(i)
            s.push(i)
        else:
            if s.isEmpty():
                balance = False
                break
            else:
                pop = s.pop()
                if (pop == '(' and i == ')') or (pop == '{' and i == '}') or(pop == '[' and i == ']'):
                    pass
                else:
                    balance = False 
                    break
 
    if not s.isEmpty():
        balance = False

    return balance


print(brackets_matching("{[]({)})}"))