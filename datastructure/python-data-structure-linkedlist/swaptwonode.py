#交换链表两两相邻节点，被交换过的不再交换，且不能只是交换节点的值，而是要进行节点的交换

"""
问题解析：1，2，3，4交换后变成2，1，4，3
算法分析：添加一个节点进行过度即可
"""



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        new_link = ListNode(-1)

        new_link.next = head 
        curr = new_link

        while curr.next and curr.next.next:
            first = curr.next
            last = curr.next.next

            curr.next = last
            first.next = last.next
            last.next = first
            curr = curr.next.next
        return new_link.next

"递归的方法下回再写，我都恨死递归了，每回写一个正确的递归，得花掉我好长时间"
