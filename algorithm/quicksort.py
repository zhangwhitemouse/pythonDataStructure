#快速排序

"""
算法思想：首先选取一个基准值pivot，然后从序列尾端开始遍历，找到比基准值小的数，放到序列左边
    然后从序列首端开始遍历，将大于基准值的数放到序列右边
    然后对基准值左右两边的子序列进行快速排序（递归）
"""

def quick_sort(arr,start,end):
    #特殊情况和边界情况判断
    if not arr or start > end:
        return
    left = start
    right = end
    pivot = arr[left]
    #只要左指针小于右指针
    while start < end:

        while start < end and arr[end] > pivot:
            end -= 1
        arr[start] = arr[end]
        while start < end and arr[start] <= pivot:
            start += 1
        arr[end] = arr[start]
        arr[start] = pivot

        quick_sort(arr,left,start - 1)
        quick_sort(arr,start + 1,right)
arr = [3,1,2,5,4]
quick_sort(arr,0,len(arr) - 1)
print(arr)
