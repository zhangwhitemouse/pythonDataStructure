#反转链表
"""
问题分析：反转链表就是将单链表的每个节点的指针域指向前一个节点，头节点特殊一点，它需要指向None
算法分析：第一反应就是暴力解法呀，就是将单链表的每个元素拿出来放入列表，然后再构建一遍链表（被自己蠢到了哈哈哈）。
    然后想了想发现我用两个变量，一个存储当前节点，一个存放当前节点的前一个节点不就行了
"""

# class Solution:
#     def reverseList(self, head):
#         prev = None
#         curr = head

#         while curr != None:
#             temp = curr.next
#             curr.next = prev
#             prev = curr
#             curr = temp

#         return prev


"""
还有一种递归的方法，但是由于我递归理解的比较差，暂时脑袋还转不过来
等我转好了，我再写哦
时间一分一秒的过去，就这样一直过了一下午，灵光乍现，懂了
"""



class Solution:
    def reverseList(self, head):
        if head == None or head.next == None:
            return head

        new_linkedlist = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return new_linkedlist