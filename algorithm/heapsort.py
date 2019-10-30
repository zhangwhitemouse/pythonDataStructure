#堆排序
"""
堆排序建立在堆这种数据结构的基础上，拿一组序列来说，先将这组序列转换成最大堆（最小堆），
然后将序列的第一个（最大值）和最后一个值进行交换，这样序列的最后一个就有序了，然后对序列剩下的元素
再调整，形成最大堆，再次交换元素，重复这一步骤直到堆中只有一个元素。
"""

def LEFT(i):
    return 2*i + 1
def RIGHT(i):
    return 2*i + 2
#********** 调整大顶堆 **********
#L:待调整序列 length: 序列长度 i:需要调整的结点
def adjust_max_heap(L,length,i):
#定义一个int值保存当前序列最大值的下标
    largest = i
#执行循环操作：两个任务：1 寻找最大值的下标；2.最大值与父节点交换
    while (1):
#获得序列左右叶子节点的下标
        left,right = LEFT(i),RIGHT(i)
#当左叶子节点的下标小于序列长度 并且 左叶子节点的值大于父节点时，将左叶子节点的下标赋值给largest
        if (left < length) and (L[left] > L[i]):
            largest = left
            print('左叶子节点')
        else:
            largest = i
#当右叶子节点的下标小于序列长度 并且 右叶子节点的值大于父节点时，将右叶子节点的下标值赋值给largest
        if (right < length) and (L[right] > L[largest]):
            largest = right
            print('右叶子节点')
#如果largest不等于i 说明当前的父节点不是最大值，需要交换值
        if (largest != i):
            temp = L[i]
            L[i] = L[largest]
            L[largest] = temp
            i = largest
            print(largest)
            continue
        else:
            break
#********** 建立大顶堆 **********
def build_max_heap(L):
    length = len(L)
    for x in range((int)((length-1)/2),-1,-1):
        adjust_max_heap(L,length,x)
#********** 堆排序 **********
def heap_sort(L):
#先建立大顶堆，保证最大值位于根节点；并且父节点的值大于叶子结点
    build_max_heap(L)
#i：当前堆中序列的长度.初始化为序列的长度
    i = len(L)
#执行循环：1. 每次取出堆顶元素置于序列的最后(len-1,len-2,len-3...)
#         2. 调整堆，使其继续满足大顶堆的性质，注意实时修改堆中序列的长度
    while (i > 0):
        temp = L[i-1]
        L[i-1] = L[0]
        L[0] = temp
#堆中序列长度减1
        i = i-1
#调整大顶堆
        adjust_max_heap(L,i,0)