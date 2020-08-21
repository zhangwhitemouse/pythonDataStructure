"""
斐波那契数列
"""

def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

