"""
数组重排序，奇数放左边，偶数放右边
思想：使用两个指针
"""

def arrar_resort(arr):

    if not arr or len(arr) <= 1:
        return arr

    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] % 2 == 0:
            if arr[right] % 2 ==0:
                right -= 1
            else:
                arr[left],arr[right] = arr[right],arr[left]
        else:
            left += 1

    return arr

print(arrar_resort([1,4,8,2,5,9]))