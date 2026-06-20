arr = [10, 5, 3,5, 4, 3, 6]
my_dict = {}
x = 0
for i in range(len(arr)):
    if arr[i] in my_dict:
        my_dict[arr[i]] += 1
    else:
        my_dict[arr[i]] = 1
for num in my_dict:
    if my_dict[num] > 1:
        print(num)
        break