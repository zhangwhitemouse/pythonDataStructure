#删除链表的重复元素
"""
问题分析：保证链表中没有重复的元素
算法分析：一边遍历一边判断，看当前节点值与前一个节点值是否相同，
    若相同，则删除当前节点，若不相同，则继续遍历
"""

class Solution(object):
    def deleteDuplicates(self, head):
        cur = head 
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head

