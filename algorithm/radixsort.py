#基数排序

"""
基数排序是桶排序的拓展，先按照整数的个位数排序，然后按照十位排序，一次往上。对于整数长度不同的情况，缺失位补0即可
"""

def radix_sort(L):
    max_len = len(str(max(L)))      #最大数的位数

    for i in range(max_len):        #循环的次数
        bucket = [[] for _ in range(10)]    #初始化桶
        for num in L:
            bucket[int(num // (10 ** i) % 10)].append(num)  #按照个位数的大小，一次放入桶的相应位置

        #print(bucket)
        L.clear()           #对每一次的排序进行组合，放入原来的序列中
        for num in bucket:
            #print(num)
            L = L + num
            #print(L)
        
    return L 


larray = [91,110,25,53,75,43,82,6,38,57]

larray = radix_sort(larray)

print(larray)
