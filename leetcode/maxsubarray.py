"""
连续子序列最大和
思想：动态规划，将每个数组元素都存放成当前最大连续子序列的和
"""

def maxSubArray(arr):

    max_sum = arr[0]

    for i in range(1,len(arr)):
        last_num = arr[i-1]

        if last_num > 0:
            arr[i] += last_num

        max_sum = max(max_sum,arr[i])

    return max_sum
