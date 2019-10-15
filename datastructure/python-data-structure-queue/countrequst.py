#计算三秒前到当前时间的请求次数

"""
问题描述：只有一个方法：ping(int t)，其中 t 代表以毫秒为单位的某个时间。
        返回从 3000 毫秒前到现在的 ping 数。
算法分析：
    来一个请求就放入队列，如果当前请求和前面的请求时间超过3秒，就移除前面的请求
    最后返回请求的次数
"""

class RecentCounter:

    def __init__(self):
        self.queue = []
        

    def ping(self, t):
        self.queue.append(t)
        while self.queue[0] < t - 3000:
            self.queue.pop(0)
        
        return len(self.queue)