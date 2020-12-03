"""
斐波那契的学习与优化
"""


def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


"""加上备忘录，使算法复杂度更低"""


def fib2(n):
    if n < 1:
        return 0

    # 备忘录初始化
    memo = [0] * (n + 1)

    return helper(memo, n)


def helper(memo, n):
    # base case
    if n == 1 or n == 2:
        return 1
    # 查备忘录
    if memo[n] != 0: return memo[n]
    # 递归计算
    memo[n] = helper(memo, n - 1) + helper(memo, n - 2)
    return memo[n]


"""Dp 的解法（自底向上）"""


def fib3(n):
    if n < 1: return 0
    if n == 1 or n == 2: return 1

    dp = [0] * (n+1)

    # base case
    dp[1] = dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
