arr= [1, 2, 3, 4, 5, 6, 7, 8]
k = 3
rev = []
for i in range(0,len(arr),k):
    rev.extend(arr[i:i+k][::-1])
print(rev)
