#最小栈
"""
问题描述：
    获取栈内的最小元素
"""

#解法一：直接使用for循环进行迭代
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []

    def push(self, x: int) -> None:
        self.items.append(x)

    def pop(self) -> None:
        self.items.pop()

    def top(self) -> int:
        return self.items.pop()

    def getMin(self) -> int:
        min = self.items[1]
        for i in self.items:
            if i < min:
                min = i
        return min


min = MinStack()
min.push(1)
min.push(7)
min.push(2)
min.push(4)

print(min.getMin())


#方法二：使用两个栈，一个数据栈，一个辅助栈
#辅助栈同步数据栈的数据

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.helper = []

    def push(self, x: int) -> None:
        self.data.append(x)
        if len(self.helper) == 0 or x <= self.helper[-1]:
            self.helper.append(x)
        else:
            self.helper.append(self.helper[-1])

    def pop(self) -> None:          
        if self.data:
            self.helper.pop()
            self.data.pop()


    def top(self) -> int:
        if self.data:
            return self.data[-1]

    def getMin(self) -> int:
        if self.helper:
            return self.helper[-1]

"""
在同步栈的过程中，需要注意保持两个栈中元素相同
"""