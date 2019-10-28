#链表的下一个更大节点

"""
问题分析：对于一个链表，针对链表中的每一个节点，找到距离它最近的第一个比他大的节点，并放入数组
    如果后面的节点中，没有比它大的，就在数组中加 0。

算法分析：如果通过暴力解法，对于链表中的每一个节点，遍历这个节点后面的节点，到找到第一个比他大的就停止
        遍历完找不到就+0
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def nextLargerNodes(self, head):
        answer = []

        cur = head
        curnext = None 
        while cur:
            curnext = cur.next
            while curnext:
                if curnext.val > cur.val:
                    answer.append(curnext.val)
                    break
                curnext = curnext.next
            if curnext == None:
                answer.append(0)
            
            cur = cur.next
        
        return answer


"""
此一方法结果是对了，但是超出了时间限制，怎么办呢？？？
我们可以借助一个栈，栈中存放数组的索引。首先将链表全部转换成数组，然后初始化answer数组，全部为0
    再进行判断，如果后面的元素大于前面的元素，则替换answer数组中的值
"""

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        length = 0
        p = head
        while p != None:
            length += 1
            p = p.next
        ori = [0 for i in range(length)]
        p = head
        for i in range(length):
            ori[i] = p.val
            p = p.next

        stack = [0]
        ans = [0 for i in range(length)]
        for i in range(1, length):
            while stack and ori[i] > ori[stack[-1]]:
                ans[stack[-1]] = ori[i]
                stack.pop()
            stack.append(i)

        return ans