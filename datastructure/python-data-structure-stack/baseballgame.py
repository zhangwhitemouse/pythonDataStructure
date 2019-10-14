#棒球比赛计分
"""
问题分析：针对不同的操作符，执行不同的操作
算法分析：第一反应是暴力解法,但是发现这个是要遵循固定顺序的（for循环好像也有顺序哦）
"""

from python_stack import Stack

class Solution:
    def calPoints(self, ops):
        s = Stack()
        count = 0

        for i in ops:
            if i == "+":
                last = s.pop()
                sec = s.peek()
                s.push(last)
                s.push(last + sec)
            elif i == "D":
                s.push(s.peek() * 2)
            elif i == "C":
                s.pop()
            else:
                s.push(int(i))

        for i in range(s.size()):
            count += s.pop()

        return count

ss = Solution()
print(ss.calPoints(["5","-2","4","C","D","9","+","+"]))