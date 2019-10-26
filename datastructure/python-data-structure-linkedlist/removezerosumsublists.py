#从链表中删除总值和为0的节点，一直删到链表中不存在这样的序列

"""
问题分析：这个我也说不清，直接上示例：[1,2,-3,3,1]      [3,1]
算法分析：为了方便，使用一个哑节点，并且使用一个字典来存储相应和的位置
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeZeroSumSublists(self, head):
        newhead = ListNode(0)
        newhead.next = head
        flag = True

        while flag:
            cur = newhead
            sum = 0
            d = {0:newhead}
            flag = False

            while cur.next:
                cur = cur.next
                sum += cur.val
                if sum in d:
                    d[sum].next = cur.next
                    flag = True
                    break

                d[sum] = cur

        return newhead.next
