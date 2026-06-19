arr = [1, 1, 2, 2, 3, 3, 4, 5, 6, 7]

my_dict = {}
for num in arr:
    if num in my_dict:
        my_dict[num] += 1
    else:
        my_dict[num] = 1

count = 0
for i in my_dict:
    if my_dict[i] == 1:
        count += 1
print(count)