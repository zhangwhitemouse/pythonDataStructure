#删除链表的重复元素
"""
问题分析：保证链表中没有重复的元素(保证没有相邻的元素存在相同)
算法分析：一边遍历一边判断，看当前节点值与前一个节点值是否相同，
    若相同，则删除当前节点，若不相同，则继续遍历
"""

# class Solution(object):
#     def deleteDuplicates(self, head):
#         cur = head 
#         while cur and cur.next:
#             if cur.val == cur.next.val:
#                 cur.next = cur.next.next
#             else:
#                 cur = cur.next

#         return head


"""
问题延伸：上面删除链表的重复节点是删除多出来的一个节点，而现在要求只要这个元素出现了重复元素，删除这个元素的所有值
例如：1,2,3,3,4     第一个问题结果:1，2，3，4   第二个结果：1，2，4

保证整个链表中，出现过相同元素的直接全部删除
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        newlink = ListNode(-1)
        newlink.next = head
        prev = None 
        cur = newlink

        while cur:
            pre = cur 
            cur = cur.next

            while cur and cur.next and cur.val == cur.next.val:
                tmp = cur.val 
                while cur and tmp == cur.val:
                    cur = cur.next
                
                pre.next = cur

        return newlink.next

