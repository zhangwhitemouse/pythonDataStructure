class Queue(object):
    "使用python列表实现队列"

    def __init__(self):
        "初始化一个空队列"
        self.items = []
        
    def isempty(self):
        "判断队列是否为空"
        return self.items == []

    def enqueue(self, item):
        "添加元素进队列"
        self.items.insert(0,item)
        #self.items.append(item)

    def dequeue(self):
        "从队列中移除元素"
        return self.items.pop()
        #return self.items.pop(0)

    def size(self):
        "返回队列中元素个数"
        return len(self.items)


"""
这里有一个小tricks：
    刚开始在实现enqueue的方法的时候，使用的是append，直接将元素添加到列表的结尾
    然后在使用dequeue方法的时候，每次弹出列表开头。
    然后才改用现在的方法，将新添加的元素直接放在列表开头，队列中取得时候直接
    pop，这样方便很多。。
    反正都可以，随便怎么实现拉
"""

