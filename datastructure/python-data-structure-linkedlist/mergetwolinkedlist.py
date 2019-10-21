#合并两个有序链表

"""
问题：两个链表都是有序的，然后将两个链表再有序的组合起来；新链表包含两个链表的所有元素
算法分析：可以同时遍历两个链表，然后将两个链表的值进行比较；当某一个链表到达末尾时，只需要
    将没有到达末尾的链表的后面元素直接拼接上来就可以了（链表有序）

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        new_link = ListNode(-1)
        prev = new_link

        while l1 and l2:

            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next

            prev = prev.next

        prev.next = l1 if l1 is not None else l2

        return new_link.next
