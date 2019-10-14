#问题描述：约瑟夫问题
"""
问题展开：
    一群人围城一个圈，指定一个人为第一个人，商定数到某个数字的人出列，直到还剩下一个人
算法分析：
    通过队列，将一群人全部放入队列，然后依次出队列，然后添加到队列尾部，到指定数字时，不添加，直接删除
"""

from python_queue import Queue

def joseph_problem(numlist,num):
    "解决约瑟夫问题(看最后还剩下谁)"
    q = Queue()

    for i in numlist:
        q.enqueue(i)

    while q.size() > 1:
        count = 1
        while not count == num:
            tmp = q.dequeue()
            q.enqueue(tmp)
            count += 1
        q.dequeue()

    return q.dequeue()

numlist = ["1","2","3","4"]

print(joseph_problem(numlist,3))
