nums = [1,2,3,4]
n = len(nums)
output = [1]*n
for i in range(1,n):
    output[i] = output[i-1] * nums[i-1]
print(output)
suffix = [1]*n
for i in range(n-2,-1,-1):
    suffix[i] = suffix[i+1] * nums[i+1]
    total = [1]*n
print(suffix)   
for i in range(n):
    total[i] = output[i] * suffix[i]
print(total)
                