#单链表的中间节点
"""
问题分析：给你链表的头节点，找到链表的中间节点，
    如果中间节点有2个，返回第二个中间节点
算法分析：
    第一反应是链表太不好找了，如果是数组该有多好呀，所以就有了第一种方法。
    将链表中的所有元素按序添加到数组中

    然后想了一下，好像还可以用快慢指针。两个指针同时开始，慢指针一次走一步，快指针一次走两步
    当快指针到结尾的时候，慢指针不就刚好到中间吗？
"""

# class Solution:
#     def middleNode(self, head):
#         arr = [head]

#         while arr[-1].next != None:
#             arr.append(arr[-1].next)

#         return arr[len(arr) // 2]


# class Solution:
#     def middleNode(self, head):
#         low = head
#         fast = head 
#         while fast != None and fast.next != None:
#             low = low.next
#             fast = fast.next.next

#         return low


"""
然后问题升级了：
    那如果我想要找到倒数第N个节点呢？
    我个人觉得是这样的：直接一次遍历，当某个人节点的node.next.next == None了,就找到这个节点了
    但是感觉这个问题没啥意义

问题变成：
    如何删除链表的第N个节点？
    从删除倒数第二个开始，然后抽象化
    使用两个指针，其中low指针比fast指针慢一步，当fast.next.next==None时，
    fast节点就是要删除的节点
"""
# class Solution:
#     def removeNthFromEnd(self, head):
#         "删除倒数第二个节点"
#         low = None
#         fast = head

#         #找到要删除的节点
#         while fast.next.next != None:
#             low = fast
#             fast = fast.next
        
#         #删除节点
#         low.next = fast.next
#         return head 


"""
我觉得抽象化后，两个指针距离为n,当快指针的下一个节点为尾节点，慢指针的下一个节点就是要删除的节点
重点关注边界情况，我这边界这里想了挺久的
"""
class Solution:
    def removeNthFromEnd(self, head, n):
        "删除倒数第N个节点"

        low = head
        fast = head

        for i in range(n):
            fast = fast.next

        #如果删除的是头节点
        if not fast:
            return head.next

        while fast.next:
            low = low.next
            fast = fast.next

        if low.next.next:    
            low.next = low.next.next
        #如果删除的是尾节点
        else:
            low.next = None
        
        return head

        

            



        
