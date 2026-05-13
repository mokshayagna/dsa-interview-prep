a = [2,1,5,3,4]
prefix = [0]*len(a)
prefix[0] = a[0]
for i in range(1,len(a)):
    prefix[i] = prefix[i-1] + a[i]
print(prefix)
suffix = [0]*len(a)
suffix[-1] = a[-1] #4
for i in range(len(a)-2,-1,-1):
    suffix[i] = suffix[i+1] + a[i]
print(suffix)
