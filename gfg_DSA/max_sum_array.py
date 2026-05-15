a = [100, 200, 300, 400]
k = 2
n = len(a)
window_sum = 0
max_sum = 0

for i in range(k):
    window_sum = window_sum + a[i]
max_sum = window_sum

for i in range(1,n-k+1):
    max_sum = max_sum - a[i-1] + a[i+k-1]
    max_sum = max(max_sum,window_sum)
print(max_sum)
