#删k个相邻的重复元素

"""
问题分析：给定一个字符串，删除字符串中k个相邻的元素，需要对S进行多次的删除操作，直到无法执行删除
    例如：s = "deeedbbcccbdaa", k = 3    删除后：s = "aa"

算法分析：我使用一个栈，栈中的每个元素都是一个数组，数组的第一个元素表示字符，第二个元素表示字符出现的次数
"""

class Solution:
    def removeDuplicates(self, s, k):
        stack = []

        for x in s:
            if not stack or stack[-1][0] != x:
                stack.append([x,1])
            elif stack[-1][1] + 1< k:
                stack[-1][1] += 1
            else:
                stack.pop()

        ans = ""

        for c, n in stack:
            ans += c*n
        return ans
