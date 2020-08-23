"""
调整排列（360笔试）
输入 4 3
1 2 1
输出2 1 4 3
"""

def change(arr):
    for i in range(0,len(arr),2):
        arr[i],arr[i+1] = arr[i+1],arr[i]
    return arr

def first_to_last(arr):
    first = arr.pop(0)
    arr.append(first)
    return arr


N,M = input().split()

arr = []
for i in range(int(N)):
    arr.append(i+1)

method = input().split()
for i in method:
    if i == '1':
        first_to_last(arr)
    if i == '2':
        change(arr)

for i in arr:
    print(i,"",end="")