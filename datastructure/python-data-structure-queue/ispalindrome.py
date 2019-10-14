#问题描述：是否为回文字符

"""
问题解析：
    回文字符串的意思就是一个字符串的首尾字母是一样的，如 rmar
算法分析：
    将整个字符串放入双端队列中，此时双端队列就是和队列一样的功能
    然后取出首尾字符进行比较，这个时候就用到了双端队列的功能了
"""
from python_deque import Deque

def is_palindrome(character):
    "是否为回文字符串"

    balance = False
    deque = Deque()

    for i in character:
        deque.addrear(i)

    front = deque.removefront()
    rear = deque.removerear()

    if front == rear:
        balance = True

    return balance

print(is_palindrome("awer"))

