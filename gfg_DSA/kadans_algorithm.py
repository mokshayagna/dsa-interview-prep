arr= [2, 3, -8, 7, -1, 2, 3]

l = 0
total = 0
answer = 0
for r in range(0,len(arr)):
    total = total + arr[r]
    answer = max(total,answer)
    if total <= 0:
        total = 0
        l = r+ 1
print(answer)
