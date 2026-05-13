a = [3,1,7,8,4,6,5]
b = []
#brutal Approach
"""
for i in range(len(a)):
    ma = a[i]
    for j in range(i,len(a)):
        ma = max(ma,a[j])
    if(ma == a[i]):
        b.append(a[i])
print(b[-1])
"""

# efficient approach
ma = a[-1]
for i in range(len(a)-1,-1,-1):
    ma = max(ma,a[i])
    
    if ma == a[i]:
        b.append(a[i])
b.reverse()
print(b)