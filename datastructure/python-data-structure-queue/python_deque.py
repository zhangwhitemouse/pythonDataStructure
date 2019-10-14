class Deque(object):
    "使用python列表实现双端队列"
    def __init__(self):
        "双端队列的初始化"
        self.items = []

    def isempty(self):
        "判断是否为空"
        return self.items == []

    def addfront(self,item):
        "在对首增加元素"
        self.items.insert(0,item)

    def addrear(self,item):
        "在队尾增加元素"
        self.items.append(item)

    def removefront(self):
        "移除队首元素"
        return self.items.pop(0)

    def removerear(self):
        "移除队尾元素"
        return self.items.pop()

    def size(self):
        "返回队列长度"
        return len(self.items)

