#删除链表的节点，但是做了一些限制

"""
问题解析：首先限定链表至少有两个节点，且删除的节点不是尾节点，只给你要删除的节点
算法分析：常规思路是修改这个节点的前一个节点的指针域，删除节点，但是现在我们无法获得前一个指针
    所以得改变思路，修改要删除节点得值，然后再将当前节点的指针域指向下一个节点的指针域指向的地址
"""

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next