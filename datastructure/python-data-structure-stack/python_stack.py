class Stack(object):
    "使用python的列表实现栈的功能"

    def __init__(self):
        "初始化一个栈"
        self.items = []

    def isEmpty(self):
        "判断是否为空"
        return self.items == []

    def push(self,item):
        "往栈中添加元素"
        self.items.append(item)    

    def pop(self):
        "删除栈顶元素，并返回该元素"
        return self.items.pop()

    def peek(self):
        "返回栈顶元素"
        return self.items[len(self.items) - 1]

    def size(self):
        "查看栈的大小"
        return len(self.items)


 

