import heapq
nums = [1,1,1,2,2,3,]
k = 2
d = {}
for num in nums:
    if num in d:
        d[num] += 1
    else:
        d[num] = 1
heap = []
for num,f in d.items():
    heapq.heappush(heap,(f,num)) # least freq comes at the top
    if len(heap) > k:
        heapq.heappop(heap)
print(heap)

result = []

while heap:
    result.append(heapq.heappop(heap)[1])

print(result)
