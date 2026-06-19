arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 14

count = 0
my_dict = {}
for i in range(len(arr)):
    my_dict[arr[i]] = 1

seen = set()
for num in arr:
    rem = sum - num
    if rem in seen:
        count += 1
        seen.add(num)
print(count)
