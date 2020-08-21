"""
给你一个列表，求列表中的三个数加起来为0，而且不能重复
"""
def threesum(arr):

    res = []
    l = 0
    r =0

    if (len(arr) < 3 or not arr):
        return res
    #对arr进行排序
    arr = sorted(arr)
    print(arr)

    for i in range(len(arr)):
        if arr[i] > 0:
            return res
        if(i > 0 and arr[i] == arr[i-1]):
            continue
        l = i + 1
        r = len(arr) - 1
        while l < r:
            sum = arr[i] + arr[l] + arr[r]

            if sum == 0:
                res.append([arr[i],arr[l],arr[r]])
                while (l < r and arr[l] == arr[l + 1]):
                    l += 1
                while(l < r and arr[r] == arr[r -1]):
                    r -= 1
                l += 1
                r -= 1
            elif sum > 0:
                r -= 1
            else:
                l += 1
    return res

arr = [1,-2,-1,0,2,3,5]
print(threesum(arr))