nums = [1, 2, 3, 4, 5, 6, 7, 8]
queries = [[0,7], [1,3], [4,6]]
# l = []
# s = 0
# for pair in queries:
#     i = pair[0]
#     j = pair[1]
#     print(i, j)
#     while i < j+1:
#         s += nums[i]
#         i += 1
#     l.append(s)
#     s = 0
# print(l)

# Build prefix sum
prefix = [0] * len(nums)
prefix[0] = nums[0]

for i in range(1, len(nums)):
    prefix[i] = prefix[i-1] + nums[i]
    
result = []

for l, r in queries:
    if l == 0:
        result.append(prefix[r])
    else:
        result.append(prefix[r] - prefix[l-1])

print(result)