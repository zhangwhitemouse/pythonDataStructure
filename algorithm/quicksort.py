#快速排序

"""
算法思想：首先选取一个基准值pivot，然后从序列尾端开始遍历，找到比基准值小的数，放到序列左边
    然后从序列首端开始遍历，将大于基准值的数放到序列右边
    然后对基准值左右两边的子序列进行快速排序（递归）
"""

def quick_sort(L,start,end):
    if start >= end:
        return

    left = start
    right = end
    pivot = L[left]

    while left != right:
        while left < right and L[right] >= pivot:
            right -= 1
        L[left] = L[right]

        while left < right and L[left] < pivot:
            left += 1
        L[right] = L[left]

    L[left] = pivot
    quick_sort(L,start,left - 1)
    quick_sort(L,right + 1,end)


larray = [9,1,2,5,7,4,8,6,3,5]

quick_sort(larray,0,9)

print(larray)