#判断是否是回文链表

"""
问题解析：就是给你一个字符串，然后看首尾节点值是否一致
算法分析：直接遍历字符串，判断头节点和尾节点的值
"""


# class Solution:
#     def isPalindrome(self, head):
#         cur = head
#         while cur.next != None:
#             cur = cur.next

#         if cur.val == head.val:
#             return True
#         return False

"""
我只能说我太天真了，我把回文链表的意思弄错了。
回文链表的意思是：链表的首节点和尾节点相同，第二个节点和倒数第二个节点相同，
    依次推下去，每两个都需要相同。

算法解析：
    第一种方法：直接将链表转换成列表（感觉所有的链表题都可以这样做哎），这里就不写了
    第二种方法：通过快慢指针法。    
"""

class Solution:
    def isPalindrome(self, head):
        low = head 
        fast = head

        while fast and fast.next:   #链表为偶数个时，fast为None，为奇数个时fast是尾节点
            low = low.next
            fast = fast.next.next

        if fast:            #链表为奇数个节点，需要将low往下移一个
            low = low.next

        new_link = None
        cur = low

        while cur:
            temp = cur.next
            cur.next = new_link
            new_link = cur
            cur = temp

        while head and new_link:
            if head.val != new_link.val:
                return False
            head = head.next
            new_link = new_link.next

        return True
