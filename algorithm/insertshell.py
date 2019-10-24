#希尔排序

"""
算法分析：希尔排序在直接插入排序的基础上进行排序
    首先将数组元素按照步长gap进行分组，分成若干个组，对每个组内的数进行直接插入排序（组内一般就是两个数）
    gap刚开始为数组长度的一半，然后每次折半，gap=1的时候，是最后一次循环分组。
    如：数组长度为10的话，第一次gap=5，就是将索引为0和索引为5进行比较，1，6和2，7和3，8和4，9
"""

def insert_shell(L):
    gap = len(L) // 2
    while gap >= 1:
        for x in range(gap,len(L)):
            for i in range(x - gap, -1, -gap):
                if L[i] > L[i + gap]:
                    temp = L[i + gap]
                    L[i + gap] = L[i]
                    L[i] = temp

        gap = gap // 2

        
larray = [9,1,2,5,7,4,8,6,3,5]

insert_shell(larray)

print(larray)            