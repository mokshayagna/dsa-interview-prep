a = [100, 200, 300, 400]
k = 2
n = len(a)
sum = 0
ans = 0

for i in range(k):
    ans = ans+a[i]
sum = ans
for i in range(i+k-1):
    sum = sum - a[i-1] + a[i+k-1]
    ans = max(ans,sum)
print(ans)
        