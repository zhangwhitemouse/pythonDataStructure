#反转括号间的字符

"""
问题分析：给定一个由括号和字符组成的字符串，按照括号的顺序，依次反转括号中的内容，最后返回字符串（不带括号）
    如："(u(love)i)"   输出 "iloveu"        "(ed(et(oc))el)"    输出"leetcode"

算法分析：第一反应就是应该会用到栈，就顺着这个方向想。每遇到一个（ 就往栈中压入一个空串，遇到一个）括号就反转栈顶元素，并压入回栈，
        其他元素则直接压入栈
"""

class Solution:
    def reverseParentheses(self, s):
        stack = [""]

        for i in s:
            if i == "(":
                stack += [""]
            elif i == ")":
                stack[-2] += stack[-1][::-1]    #从后向前，步进值为1
                stack.pop()
            else:
                stack[-1] += i

        return stack[0]