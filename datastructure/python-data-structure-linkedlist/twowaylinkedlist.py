#软柿子捏完了，开始了双链表(单向)

class Node(object):
    "实现一个节点类"

    def __init__(self,data):
        "一个节点有3个属性"
        self.data = data
        self.prev = None
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self,newdata):
        self.data = newdata

    def get_next(self):
        return self.next

    def set_next(self,newnext):
        self.next = newnext

    def get_prev(self):
        return self.prev

    def set_prev(self,newprev):
        self.prev = newprev


class Two_Way_LinkedList(object):
    "实现双向链表"

    def __init__(self):
        "设置头节点"
        self.head = None

    def isempty(self):
        "判断链表是否为空"
        return self.head == None

    def size(self):
        "链表长度"
        count = 1
        cur = self.head
        while cur.get_next() != None:
            count += 1
            cur = cur.get_next()
    
    def search(self,data):
        "判断元素是否存在"
        cur = self.head
        while cur.get_next() != None:
            if cur.get_data() == data:
                return True
            cur = cur.get_next()
        if cur.get_data() == data:
            return True
        return False

    def add(self,data):
        "增加一个节点（头部添加）"
        new_node = Node(data)

        #如果是空链表
        if self.isempty():
            # new_node.set_next(self.head)
            # new_node.set_prev(self.head)
            self.head = new_node
        else:
            new_node.set_next(self.head)
            self.head.set_prev(new_node)
            self.head = new_node

    def append(self,data):
        "增加一个节点（尾部添加）"
        new_node = Node(data)

        #如果是空链表
        if self.isempty():
            self.head = new_node
        else:
            cur = self.head
            while cur.get_next() != self.head:
                cur = cur.get_next()
            new_node.set_prev(cur)
            cur.set_next(new_node)

    def remove(self,data):
        "删除值为data的节点"
        cur = self.head

        #如果头节点就是要删除的元素
        if cur.get_data() == data:
            #链表只有一个节点
            if cur.get_next() == None:
                self.head = None
            else:
                cur.get_next().set_prev(None)
                self.head = cur.get_next()
        
        #如果要删除的节点处于链表中间
        else:
            previous = self.head
            while cur.get_next() != None:
                if cur.get_data() == data:
                    previous.set_next(cur.get_next())
                    cur.get_next().set_prev(previous)
                else:
                    previous == cur
                    cur = cur.get_next()
            if cur.get_next() == None:
                previous.set_next(cur.get_next())






    