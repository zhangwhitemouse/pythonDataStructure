# 用队列实现栈

"""
问题分析：队列是先进先出的而栈是先进后出的
算法分析：我觉得最好的方式就是通过双端队列来实现
"""
from python_deque import Deque
class MyStack(object):

    def __init__(self):
        self.stack = Deque()

    def isempty(self):
        return self.stack.isempty()

    def push(self,item):
        self.stack.addfront(item)

    def pop(self):
        return self.stack.removefront()

    def peek(self):
        return self.stack.removefront()

stack = MyStack()

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())
print(stack.peek())