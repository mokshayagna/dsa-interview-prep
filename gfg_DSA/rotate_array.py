arr = [1, 2, 3, 4, 5]
# [3, 4, 5, 1, 2]
d = 2
c = d % len(arr)
print(arr[d:] + arr[:d]) 
