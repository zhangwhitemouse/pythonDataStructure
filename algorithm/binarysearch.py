#二分查找的实现
"""
二分查找算法
"""

def binary_search(arr,item):
    """
    二分查找,arr数组必须有序
    :param arr: 查找的数组
    :param item: 带查找的数
    :return: item在arr中的索引
    """
    left = 0
    right = len(arr) - 1

    #这里=号必须得加，否则边界会有问题
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] > item:
            right = mid - 1
        elif arr[mid] < item:
            left = mid + 1
        else:
            return mid

    return None

print(binary_search([1,3,5,7,9],9))
