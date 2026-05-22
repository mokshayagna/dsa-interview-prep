a = [1,2,3,4,5]
#Output: 4
a = sorted(a)
min_val = min(num for num in a if num > 0) 
max_val = max(num for num in a if num > 0)
while min_val < max_val:
    if min_val in a:
        min_val += 1
    else:
        print(min_val)
        break
     