arr = [2,5]
sum = 10

count = 0
my_dict = {}
for i in range(len(arr)):
    my_dict[arr[i]] = 1

for num in arr:
    rem = sum - num
    if rem in my_dict:
        count += 1
print(count // 2)
