"""
给定一个数组，计算数组中的元素和的最大值，要求相邻元素不能相加
（leetcode198 打家劫舍）
动态规划的思想
"""

def max_sum(arr):
    prev = 0
    curr = 0

    for i in arr:
        curr,prev = max(prev+i,curr),curr

    return curr

arr = [5,3,2,6]

print(max_sum(arr))