#将链表向右旋转K个位置

"""
问题分析：就是将链表节点都向右移动k个元素，需要分两种情况考虑：K>链表长度，k小于链表长度
算法解析：最重要的就是表示新链表的头部和尾部
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        if head == None:
            return head
        n = 1    
        oldtail = head 
        while oldtail.next:
            
            oldtail = oldtail.next
            n += 1

        oldtail.next = head

        newtail = head
        for i in range(n - k % n - 1):      #主要就是range里面的这个公式比较难理解
            newtail = newtail.next

        newhead = newtail.next

        newtail.next = None

        return newhead
