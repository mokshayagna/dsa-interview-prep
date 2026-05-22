mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15,16]]

n = len(mat) #row
m = len(mat[0]) #coloumn
ans = []
for i in range(0,m):
    ans.append(mat[0][i])
if n > 1:
    for j in range(1,n):
        ans.append(mat[j][m-1])
for i in range(m-2,-1,-1):
    ans.append(mat[n-1][i])
if m > 1:
    for j in range(n-2,0,-1):
        ans.append(mat[j][0])
print(ans)
