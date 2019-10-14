#下一个更大元素
"""
问题描述：给定两个不含重复元素的数组，num1，num2，且num1是num2的子集
    对于num1中的每一个元素，找到在num2中的相同值，并判断此时num2中该元素后面的一个元素值
    与该元素的大小，后面出现的元素比该元素大的话，后面的元素返回，否则返回-1

算法分析：
    对两个列表进行遍历，然后再判断大小
"""

# class Solution:
#     def nextGreaterElement(self, nums1, nums2):
#         result = []   
#         for i in nums1:
#             temp = -1                       #多考虑变量的范围，之前没考虑到，导致temp变量被修改了
#             for j in nums2[nums2.index(i):]:
#                 if i < j:
#                     temp = j
#                     break
#             result.append(temp)
#         return result

"""
问题优化:对于较小的数组，暴力的循环法是能够解决的（O(n^2)），
    但是对于大的数组，这种方法的时间复杂度太高。
    所以我们下面通过栈来解决

算法分析：
    首先用Map将较小的数组（子集）映射
    然后遍历大的数组，并维护一个栈。
    在循环过程中，如果栈为空，则将循环取到的元素放入栈
    若栈不为空且栈pop出来的元素小于循环的元素，则修改Map中相应元素的映射
    然后将栈中的元素pop出来

    最后将Map中的元素形式转换成数组的格式
"""

from python_stack import Stack

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        mp = dict()
        stack = Stack()

        for j in nums2:
            while not stack.isEmpty() and stack.peek() < j:
                mp[stack.pop()] = j
            stack.push(j)
        return [mp.get(i,-1) for i in nums1]


ss = Solution()
res = ss.nextGreaterElement([4,1,2],[1,3,4,2])
print(res)        
            