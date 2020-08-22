"""
给定一个M*N由0­1组成的矩阵，是否能找到一个行的集合，使得集合中每一列都恰好包含一个1
(也可以使用高深的舞蹈链去解决)
"""

M,N = map(int,input().split())

#创建一个4行3列的二维数组
matrix = [[0]*3]*3

for i in range(M):
    row = input().split()
    for j in range(N):
        matrix[i][j] = map(int,row[j])


back = 0

for i in range(M):
    flag = 0;
    for j in range(N):
        if(matrix[j][i]==1):
            flag =1
            break
    if flag==1:
        back += 1

if back == int(N):
    print("yes")
else:
    print("No")




