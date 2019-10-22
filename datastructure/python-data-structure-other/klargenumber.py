#找到数据流中第K大的数

"""
问题描述：给你一个数组，返回指定第K大的元素（是排好序的第K大元素）
算法分析：我觉得最简单的方法就是对数组进行排序，然后返回第几大的数，就是返回相应的索引对应的值，比如返回第2大的数，索引就为1
    然后想了想，用堆也可以做；返回第几大的索引，就pop几次呗
"""

# class KthLargest:

#     def __init__(self, k: int, nums: List[int]):
#         self.k = k
#         self.nums = nums

#     def add(self, val: int) -> int:
#         self.nums.append(val)
#         new_nums = self.nums.sort(reverse = True)
#         return self.nums[self.k - 1]


import heapq
class KthLargest:
    def __init__(self, k: int, nums):
        self.pool = heapq.nlargest(k, nums)
        heapq.heapify(self.pool)
        self.k = k

    def add(self, val: int) -> int:
        if len(self.pool) < self.k:
            heapq.heappush(self.pool,val)
        else:
            heapq.heappushpop(self.pool,val)
        return self.pool[0]
