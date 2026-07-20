import heapq

arr = [12, 5, 787, 1, 23]
k = 2

heap = []
for i in range(k):
    heap.append(arr[i])
    heapq.heapify(heap) # min heap, top element will be mn value

for i in range(k,len(arr)):
    if arr[i] > heap[0]:
        heapq.heappop(heap) # popping smallest element
        heapq.heappush(heap,arr[i]) # adding next element

ans = []
while heap:
    ans.append(heapq.heappop(heap))
print(ans)