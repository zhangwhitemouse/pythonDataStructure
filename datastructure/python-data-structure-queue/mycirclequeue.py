#循环队列

"""
问题解析：设计一个循环队列。普通队列在使用数组实现的时候，队列头和队列尾固定，当队列元素装满，需要重新找一个位置
    而循环队列使用使用两个指针，元素出队时，无需移动大量的元素，只需要移动队头指针就可以了。
"""

class MyCircularQueue:

    def __init__(self, k: int):

        self.size = k        #队列长度
        self.head = 0       #头节点
        self.num = 0        #元素个数
        self.queue = [0] * self.size
        

    def enQueue(self, value: int) -> bool:

        if self.num == self.size:
            return False
        else:
            self.queue[(self.head + self.num) % self.size] = value  #元素应该放置的位置
            self.num += 1
            return True

    def deQueue(self) -> bool:

        if self.num == 0:
            return False
        else:
            self.head = (self.head + 1) % self.size #头节点向后移动一个单位
            self.num -= 1
            return True

    def Front(self) -> int:

        if self.num == 0:
            return -1
        
        return self.queue[self.head]    #返回队头元素
        

    def Rear(self) -> int:

        if self.num == 0:
            return -1

        return self.queue[(self.head + self.num - 1) % self.size]   #队尾元素的索引

    def isEmpty(self) -> bool:

        return self.num == 0

    def isFull(self) -> bool:

        return self.num == self.size



#循环双端队列
"""
循环双端队列与循环队列的主要区别在于：多了两个功能，可以在队头添加元素，可以在队尾移除元素
"""

def insertFront(self, value: int) -> bool:
        if self._num == self._len:
            return False
        self._head = (self._head - 1 + self._len) % self._len
        self._elems[self._head] = value
        self._num += 1
        return True


def deleteLast(self) -> bool:
        if self._num == 0:
            return False
        self._num -= 1
        return True
