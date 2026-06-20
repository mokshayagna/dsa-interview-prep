arr = [1, 2, 3, 2, 4, 1, 5]
my_dict = {}
l = []
for num in arr:
    if num in my_dict:
        my_dict[num] += 1
        l.append(num)
    else:
        my_dict[num] = 1
l.sort()
print(l)