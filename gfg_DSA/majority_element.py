arr = [1, 1, 2, 1, 3, 5, 1]
"""
n = len(arr) / 2
found = False
for i in range(0, len(arr)):
    count = 1
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            count += 1
    if count > n:
        print(arr[i])
        found = True
        break
if found == False:
    print(-1)
"""

n = len(arr)/2

dic = {}

for i in range(0,len(arr)):
    if arr[i] in dic:
        dic[arr[i]] += 1
    else:
        dic[arr[i]] = 1
m = max(dic.values())
for key, value in dic.items():
    if value == m and m > n:
        print(key)
print(-1)
