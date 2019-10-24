#直接插入排序

"""
算法思想：
    将数组中的每一个元素与前面排好序的数进行比较，
    如果比前面的数小，则交换
    如果比前面的数大，则停止，进入下一次循环
"""

def insert_sort(L):

    for x in range(1,len(L)):           #从1开始是因为默认数组的第一个元素已经排好序了
        temp = L[x]
        j = x - 1

        while j >=0 and temp < L[j]:
            L[j + 1] = L[j]
            j = j - 1
            L[j] = temp

            



            
