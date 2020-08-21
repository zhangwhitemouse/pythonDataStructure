#归并排序

"""
算法思想：采用分而治之的思想，对一个序列先进行划分，分为左右两部分，然后不停的递归，直到左右两边只剩下一个元素
    然后再合，最后左右两边都合并起来之后，各自是有序了，但是整体还不一定有序，所以，我们需要通过一个合并，使得整体
    有序。
"""

def mergesort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left_arr = mergesort(arr[:mid])
    right_arr = mergesort(arr[mid:])

    return merge(left_arr,right_arr)

def merge(left_arr,right_arr):

    res = []
    i = 0
    j = 0

    while i < len(left_arr) and j < len(right_arr):

        if left_arr[i] < right_arr[j]:
            res.append(left_arr[i])
            i += 1
        else:
            res.append(right_arr[j])
            j += 1

    res += left_arr[i:]
    res += right_arr[j:]

    return res

arr = [2,3,1,7,2,0]
print(mergesort(arr))




