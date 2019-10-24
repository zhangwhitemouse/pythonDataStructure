#选择排序
"""
算法思想：先设定一个最小元素，然后在待排序序列中，找到最小元素，将它们两进行比较
    如果待排序序列中的最下元素比最小元素小，则交换两个元素
"""

def select_sort(L):
    for x in range(0,len(L)):
        min = L[x]

        for i in range(x + 1,len(L)):
            if L[i] < min:
                temp = L[i]
                L[i] = min
                min = temp
        
        L[x] = min


larray = [9,1,2,5,7,4,8,6,3,5]

select_sort(larray)

print(larray)   