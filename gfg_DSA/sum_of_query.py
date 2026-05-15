n = 4
arr = [1, 2, 3, 4]
q = 2
queries = [1, 4, 2, 3]
ans = []

#brutal approach
"""
for i in range(0, len(queries)-1, 2):
    l = queries[i]
    r = queries[i+1]
    ma = 0
    for j in range(l-1, r):
        ma = ma + arr[j]
    print(ma)
"""
#efficient way
ps = [0]*n
ps[0] = arr[0]
for i in range(1,len(arr)):
    ps[i] = ps[i-1] +arr[i] #[1,3,6,10]
    
for i in range(0,len(queries)-1,2):
    l = queries[i] #1, 2
    r = queries[i+1] #4, 3
    if l == 1:
        ma = ps[r-1]
    else:
        ma = ps[r-1] - ps[l-2]
    
    print(ma) 
    
