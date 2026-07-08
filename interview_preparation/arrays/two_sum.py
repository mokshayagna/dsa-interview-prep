nums = [3,2,4]
target = 6
hash = {}
for i in range(len(nums)):
    sec = target - nums[i]
    if sec in hash:
        print([hash[sec],i])
    else:
        hash[nums[i]] = i
        