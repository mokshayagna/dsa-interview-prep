nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
i = 0
j = len(nums) - 1
while i < j:
    if nums[i] == 0:
        nums.append(nums.pop(i))
        j -= 1
    else:
        i += 1
print(nums)
