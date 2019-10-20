#判断链表是否有环

"""
问题分析：给你一个链表，需要判断链表的尾节点是否和链表中的某个节点相连
    如果不连，返回False
    如果相连，则返回True（可以知道链表尾节点连接的位置）

算法分析：遍历整个链表，将走过的链表地址都保存在一个列表中，然后在把节点往后移的时候
    先判断后移的地址是否在列表中，在就说明链表有环，不在说明没环
"""

# class Solution:
#     def hasCycle(self, head):
#         # pos = -1
#         arr = []
#         cur = head

#         if cur == None:
#             return False

#         while cur.next != None:
#             arr.append(cur)
#             for i in arr:
#                 if i == cur.next:
#                     # pos = arr.index(cur)
#                     return True
            
#             cur = cur.next

#         return False

"""
方法是可行的，但是超出了执行时间的限制。看来得想另一个办法了

想了一下超出时间限制得原因好像是对列表的for循环，当链表很长，列表不可避免的很大，造成执行时间的消耗
所以，可不可以找另一种数据结构，代替列表存储遍历过的节点呢
然后，就想到了哈希表
"""

class Solution:
    def hasCycle(self, head):
        hashtable = {head}
        if head == None:
            return False
        head = head.next

        while head != None:
            if head in hashtable:
                return True
            else:
                hashtable.add(head)
                head = head.next
        return False


"""
然后在使用哈希表的基础上，有一种置空法，思想和上面的差不多，但是不需要额外的存储空间
在遍历链表的时候，将所有链表的值设为None。
"""
            

class Solution:
    def hasCycle(self, head):

        if head == None:
            return False

        while head.next and head.val:
            head.val = None
            head = head.next

        if not head.next:
            return False
        return True