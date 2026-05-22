mat = [[1, 2, 3, 4], 
       [5, 6, 7, 8], 
       [9, 10, 11, 12], 
       [13, 14, 15, 16]]

n = len(mat) #row
m = len(mat[0]) #coloumn

sc = 0
sr = 0
lr = n-1
lc = m-1
ans = []

while sr <= lr and sc <= lc:
    for i in range(sc,lc+1):
        ans.append(mat[sr][i])
        
    for j in range(sr+1,lr+1):
        ans.append(mat[j][lc])

    if sr <= lr:
        for i in range(lc-1,sc-1,-1):
            ans.append(mat[lr][i])
    if sc <= lc:
        for j in range(lr-1,sr,-1):
            ans.append(mat[j][sc])

    sr += 1
    sc += 1
    lr -= 1
    lc -= 1
print(ans)