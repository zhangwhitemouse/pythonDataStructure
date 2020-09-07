#问题描述：使用栈来生成队列
"""
算法思想：
题目只要求实现 加入队尾appendTail() 和 删除队首deleteHead()
两个函数的正常工作，因此我们可以设计栈 A 用于加入队尾操作，栈 B 用于将元素倒序，从而实现删除队首元素。

"""
class CQueue:

    def __init__(self):
        self.A,self.B = [],[]

    def appendTail(self, value: int) -> None:
        self.A.append(value)

    def deleteHead(self) -> int:
        if not self.A:
            return -1
        if self.B:
            return self.B.pop()
        while self.A:
            self.B.append(self.A.pop())

        return self.B.pop()

