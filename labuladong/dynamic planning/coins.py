"""凑零钱问题
给你 k 种面值的硬币，面值分别为 c1, c2 ... ck，
每种硬币的数量无限，再给一个总金额 amount，
问你最少需要几枚硬币凑出这个金额，如果不可能凑出，算法返回 -1 。
"""


def coinChange(coins, amount):
    def dp(n):
        # base case
        if n < 0: return -1
        if n == 0: return 0
        # 初始化 求最小所以初始化成正无穷
        res = float("INF")

        for i in coins:
            # 子问题求解
            subploblem = dp(n - i)
            if subploblem == -1: continue

            res = min(res, subploblem + 1)

        return res if res != "INF" else -1

    return dp(amount)


"""带备忘录"""


def coinChange2(coins, amount):
    # 备忘录
    memo = dict()
    def dp(n):
        # base case
        if n < 0: return -1
        if n == 0: return 0
        # 初始化 求最小所以初始化成正无穷
        res = float("INF")

        for i in coins:
            # 子问题求解
            subploblem = dp(n - i)
            if subploblem == -1: continue

            res = min(res, subploblem + 1)

        memo[n] = res if res != "INF" else -1
        return memo[n]

    return dp(amount)


"""使用DP数组的方式"""

def coinChange3(coins, amount):
    # 初始化一个大小是amount=1的数组，默认直也是amount+1
    dp = [amount+1] * (amount+1)
    dp[0] = 0

    for i in range(amount+1):
        for coin in coins:

            if i - coin < 0:continue
            dp[i] = min(dp[i],1+dp[i-coin])

    return -1 if dp[amount] == 1 + amount else dp[amount]
