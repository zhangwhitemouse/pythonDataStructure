#柿子捡软的捏，从单链表开始呀


class Node(object):
    "实现一个节点类"

    def __init__(self,data):
        "一个节点有两个属性"
        self.data = data
        self.next = None

    def get_data(self):
        "获取节点的数据"
        return self.data

    def set_data(self,newdata):
        "更新节点数据"
        self.data = newdata

    def get_next(self):
        "获取后继节点地址"
        return self.next

    def set_next(self,newnext):
        "更新后继节点"
        self.next = newnext



class Single_LinkedList(object):
    "实现单链表"

    def __init__(self):
        "初始化，设置头节点为空"
        self.head = None

    def add(self,data):
        "增加一个节点(头部添加)"
        new_node = Node(data)           #创建一个新的节点
        new_node.set_next(self.head)    #将新节点的指针域设置为self.head(None)
        self.head = new_node            #使头节点变更成new_node

    def append(self,data):
        "增加一个节点（尾部添加）"
        new_node = Node(data)
        #如果链表是空链表
        if self.isempty():
            new_node.set_next(self.head)
            self.head = new_node
        #如果不是空链表
        else:
            cur = self.head
            while cur.get_next() != None:
                cur = cur.get_next()
            new_node.set_next(cur.get_next())
            cur.set_next(new_node)

    def search(self,data):
        "判断某个值在链表中是否存在"
        cur = self.head            #从头节点开始遍历,值相等返回True，找不到相等的返回False
        while cur.get_next() != None:
            if cur.get_data() == data:
                return True
            cur = cur.get_next()

        if cur.get_data() == data:
            return True

        return False

    def remove(self,data):
        "删除值为data的节点"
        cur = self.head
        previous = None

        while cur != None:
            if cur.get_data() == data:
                break
            previous = cur
            cur = cur.get_next()

        if previous == None:        #删除的节点是头节点
            self.head = cur.get_next()
        else:                       #删除的不是头节点
            previous.set_next(cur.get_next())
    
    def isempty(self):
        "判断是否为空"
        return self.head == None

    def size(self):
        "返回链表长度"
        count = 1 
        cur = self.head

        while cur.get_next() != None:
            count += 1
            cur = cur.get_next()

        return count

    def travel(self):
        "遍历链表"
        cur = self.head
        while cur.get_next() != None:
            print(cur.get_data())
            cur = cur.get_next()
        print(cur.get_data())

        

    



    
