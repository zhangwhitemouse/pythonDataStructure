#比较含有#（退格）的字符串
"""
问题解析：
    输入两个字符串，比较两个字符串是否相等，# 号代表回退一个字符
    如 ab#c ad#c 这两个字符串是相等的，都为ac
算法分析：
    将两个字符串都压入栈，然后比较栈中的元素
"""

from python_stack import Stack

class Solution:
    def backspaceCompare(self, S, T):
        s1 = Stack()
        s2 = Stack()
        str1 = ""
        str2 = ""

        for i in S:
            if i == "#" and not s1.isEmpty():
                s1.pop()
            elif i == "#" and s1.isEmpty():
                pass
            else:
                s1.push(i)

        for j in T:
            if j == "#" and not s2.isEmpty():
                s2.pop()
            elif j == "#" and s2.isEmpty():
                pass
            else:
                s2.push(j)

        for k in range(s1.size()):
            str1 = str1 + s1.pop()
        for n in range(s2.size()):
            str2 = str2 + s2.pop()

        return str1 == str2


ss = Solution()
print(ss.backspaceCompare("y#fo##f","y#f#o##f"))