arr = [1,2,3,7,5]
sum = 12
count = 0
my_dict = {}
prefix = 0
for i in range(len(arr)):
    prefix += arr[i]
    my_dict[prefix] = 1
    val = prefix - sum
    if val in my_dict:
        count += 1
print(count)