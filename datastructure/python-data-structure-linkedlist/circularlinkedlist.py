#下一个软柿子就是循环链表

from singlelinkedlist import Node

class Circular_LinkedList(object):
    "实现循环链表"

    def __init__(self,data):
        "初始化，设置头节点"
        self.head = None

    def add(self,data):
        "增加一个节点（头部添加）"
        new_node = Node(data)
        if self.isempty():
            self.head = new_node
            new_node.set_next(self.head)
        else:
            new_node.set_next(self.head)    #添加的节点指向head
            cur = self.head
            while cur.get_next() != self.head:
                cur = cur.get_next
            cur.set_next(new_node)
            self.head = new_node

    def append(self,data):
        "增加一个节点（尾部添加）"
        new_node = Node(data)
        #如果链表是空链表
        if self.isempty():
            self.head = new_node
            new_node.set_next(self.head)
        #不是空链表
        else:
            cur = self.head
            while cur.get_next() != self.head:
                cur = cur.get_next()
            cur.set_next(new_node)
            new_node.set_next(self.head)   
    
    def isempty(self):
        "判断是否为空"
        return self.head == None
    
    def search(self,data):
        "判断某个值在链表中是否存在"
        cur = self.head
        while cur.get_next() != self.head:
            if cur.get_data() == data:
                return True
            cur = cur.get_next()
        return False
    
    def size(self):
        "返回链表长度"
        count = 1
        cur = self.head

        while cur.get_next() != self.head:
            count += 1
            cur = cur.get_next()

        return count
    
    def travel(self):
        "遍历链表"
        cur = self.head
        while cur.get_next() != self.head:
            print(cur.get_data())
            cur = cur.get_next()
        print(cur.get_data())

    def remove(self,data):
        "删除值为data的节点"
        cur = self.head
        previous = None

        #如果头节点就是要删除的元素
        if cur.get_data() == data:
            #链表不只一个元素
            if cur.get_next() != self.head:
                while cur.get_next() != self.head:
                    cur = cur.get_next()
                cur.set_next(self.head.get_next())
                self.head = self.head.get_next()
            else:
                self.head = None
        #删除的节点不是头节点
        else:
            previous = self.head
            #删除的节点是中间节点
            while cur.get_next() != self.head:
                if cur.get_data() == data:
                    previous.set_next(cur.get_next())
                    return
                else:
                    previous = cur
                    cur = cur.get_next()
            #删除的节点是尾节点
            if cur.get_next() == self.head:
                previous.set_next(cur.get_next())