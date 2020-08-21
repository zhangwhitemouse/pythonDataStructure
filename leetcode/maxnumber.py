"""
给定一个数组，求数组中拼出的最大数
[3,30,34,5,9]
9534330

可以先将数组中的数按照字符串排序
"""

def max_number(arr):

    #先用冒泡，对数组中的元素按照字典序排序
    for i in range(len(arr) - 1):
        for j in range(i,len(arr) - i - 1):
            if str(arr[j]) + str(arr[j+1]) > str(arr[j+1]) + str(arr[j]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
    string = ''
    for i in arr:
        string = str(i) + string

    return string

arr = [3,30,34,5,9]

print(max_number(arr))


