#冒泡排序
"""
算法思想：将序列的当中的左右元素依次比较，若前一个大于后一个，则交换位置
    一次遍历下来，最后一个元素一定是序列的最大元素
    然后对剩下的n-1个元素进行比较
"""

def bubble_sort(L):
    size = len(L)

    for x in range(1,size):             #表示第几轮循环，一共n-1轮
        for i in range(0,size - x):     #每轮从0到未排序的结束
            if L[i] > L[i + 1]:
                temp = L[i]
                L[i] = L[i + 1]
                L[i + 1] = temp

larray = [9,1,2,5,7,4,8,6,3,5]
bubble_sort(larray)

print(larray)     