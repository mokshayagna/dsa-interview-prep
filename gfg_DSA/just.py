arr = [[2, 4],[1, 3],[9, 10],[6, 8]]
res = []
arr.sort(key=lambda x: x[0])

for i in arr:
    res.append(i)
print(res)