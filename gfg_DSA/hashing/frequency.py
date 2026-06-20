arr = [1, 2, 2, 3, 1, 1]

my_dict = {}
for num in arr:
    if num in my_dict:
        my_dict[num] += 1
    else:
        my_dict[num] = 1
print(my_dict)