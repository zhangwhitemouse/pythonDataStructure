#在任意位置添加括号使字符成立

"""
问题分析：针对这种问题，遇到（ 就压入栈，遇到 ）就弹出。最后看栈中还剩多少个 （
    但是现在不行，因为如果栈空了，后面紧跟着 ），再弹出的话会报错

算法分析：主要就是在原来的基础上加上一个额外的判断条件
"""

class Solution:
    def minAddToMakeValid(self, S):
        res = 0
        stack = []

        for i in S:
            if i == "(":
                stack.append("(")
            elif len(stack) == 0 and i == ")":
                res += 1

            else:
                stack.pop(len(stack) - 1)
        
        res += len(stack)
        return res