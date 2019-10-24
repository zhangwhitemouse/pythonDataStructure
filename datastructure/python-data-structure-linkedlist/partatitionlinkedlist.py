#给定一个值，将链表分成两部分

"""
问题分析：给定一个值，当链表中的元素小于这个值时，放在链表的左边，大于等于这个值时放在链表的右边
算法解析：使用两个哑节点，一个节点存放左边的链表，一个存放右边的链表，最后将两个链表拼接起来
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        left = ListNode(-1)
        right = ListNode(-2)
        prev = left
        cur = right

        while head:
            if head.val < x:
                prev.next = head
                prev = prev.next
            else:
                cur.next = head
                cur = cur.next 

            head = head.next

        #拼接两个短链表
        prev.next = right.next
        cur.next = None
        return left.next