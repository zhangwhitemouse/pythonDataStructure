#归并排序

"""
算法思想：采用分而治之的思想，对一个序列先进行划分，分为左右两部分，然后不停的递归，直到左右两边只剩下一个元素
    然后再合，最后左右两边都合并起来之后，各自是有序了，但是整体还不一定有序，所以，我们需要通过一个合并，使得整体
    有序。
"""

def mergesort(L):
    if len(L) <= 1:
        return L

    mid = len(L) // 2

    left = mergesort(L[:mid])
    right = mergesort(L[mid:])
    return merge(left,right)

def merge(left,right):
    temp = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            temp.append(left[i])
            i += 1

        else:
            temp.append(right[j])
            j += 1

    
    if i == len(left):
        for j in right[j:]:
            temp.append(j)

    else:
        for i in left[i:]:
            temp.append(i)

    return temp

larray = [9,1,2,5,7,4,8,6,3,5]

larray = mergesort(larray)

print(larray)
