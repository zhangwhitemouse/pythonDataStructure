#问题描述：使用栈来生成队列
"""
算法思想：
    利用一个临时栈，首先判断队列栈中是否有元素，没有，直接添加在队列栈中；
    有就将所有队列栈中的元素，全部通过pop的形式，压入到临时栈中，然后再将要push的
    元素先push到临时栈中，最后将所有临时栈中的元素通过pop的形式push到队列栈中。
"""
from python_stack import Stack
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.tmp = Stack()
        self.queue = Stack()
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if self.queue.isempty():
            self.queue.push(x)
        else:
            while not self.queue.isempty():
                self.tmp.push(self.queue.pop())
            self.tmp.push(x)
            while not self.tmp.isempty():
                self.queue.push(self.tmp.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.queue.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.queue.peek()

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.queue.isempty()