#两数相加

"""
问题分析：将整数存放在链表中，逆序存放且每个节点存放一个位，(2 -> 4 -> 3)就代表数字342
    然后需要将两个链表表示的数加起来，用另外一个链表存放（存放的就是整数和）

算法分析：从两个链表的头开始，依次移动，每次将两个节点的值相加，若大于10，取个位，并且下一位的相加要加上1
        小于10，则直接相加
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def addTwoNumbers(self, l1, l2):

#         new_headlist = ListNode(-1)

#         cur = new_headlist
#         bonus = 0

#         while l1 and l2:
#             temp = l1.val + l2.val + bonus
#             if temp >= 10:
#                 temp = temp % 10
#                 # cur.val = temp
#                 cur.next = ListNode(temp)
#                 cur = cur.next
#                 bonus = 1
#             else:
#                 cur.next = ListNode(temp)
#                 cur = cur.next
#                 bonus = 0
            
#             l1 = l1.next
#             l2 = l2.next

#         if l1 == None:
#             cur.next = l2

#         if l2 == None:
#             cur.next = l1
#         return new_headlist.next


"""
上面是我写的第一个版本，有点小BUG；不想改了，重新写了一个，思想都是一样的，只是改了判断条件
"""

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_head = ListNode(0)
        curry = new_head
        carry = 0
        
        while l1 or l2:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            sum += carry
            carry = sum // 10
            curr.next = ListNode(sum % 10)
            curr = curr.next
        if carry > 0:
            curr.next = ListNode(1)
        return new_head.next


        