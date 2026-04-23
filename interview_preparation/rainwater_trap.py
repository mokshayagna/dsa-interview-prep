nums = [0,1,0,2,1,0,1,3,2,1,2,1]

i = 0
j = len(nums)-1
max_area = 0
while i < j:
    width = j - i
    height = min(nums[i], nums[j])
    area = width * height
    max_area = max(max_area, area)
    if nums[i] < nums[j]:
        i += 1
    else:
        j -= 1
print(max_area)
