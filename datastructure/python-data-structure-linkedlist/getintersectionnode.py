#判断两个单向链表的相交节点

"""
问题分析：给你两个单链表，如果两个链表不相交返回Null，相交则返回相交节点的值。
算法分析：遍历第一个链表，将第一个链表的地址放入哈希表；然后开始遍历第二个链表，查看第二个链表节点的地址是否在哈希表中
"""

class Solution(object):
    def getIntersectionNode(self, headA, headB):

        table = {headA}
        if headA == None or headB == None:
            return None

        while headA != None:
            table.add(headA)
            headA = headA.next

        while headB != None:
            if headB in table:
                return headB
            else:
                headB = headB.next
        
        return None


"""
另外一种方法：两个指针，先将第一个指针遍历A链表，遍历到A链表结尾时指向B链表的头节点，继续遍历；另外一个指针从B链表的头开始遍历，
遍历到结尾，指向A链表的头，继续遍历；最后当两个指针相遇时，就是相交的节点，否则不相交。
"""