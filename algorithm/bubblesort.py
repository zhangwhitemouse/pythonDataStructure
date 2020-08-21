#冒泡排序
"""
算法思想：将序列的当中的左右元素依次比较，若前一个大于后一个，则交换位置
    一次遍历下来，最后一个元素一定是序列的最大元素
    然后对剩下的n-1个元素进行比较
"""

def bubble_sort(arr):
    if not arr:
        return
    #5个数，只需要比较4次
    for i in range(len(arr) -1):
        #设置标志位，一旦没有元素发生位置变化，说明已经有序，停止比较
        flag = False
        #比较过i次后，最后的i个数已经有序,所以无需比较
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
                flag = True
        if not flag:
            break
    return arr

arr = [9,1,2,5,7,4,8,6,3,5]

print(bubble_sort(arr))
