arr = [1, -2, 1, 0, 5]
target = 2
dic = {}
for i in range(len(arr)):
    rem = target - arr[i]
    
    if rem in dic:
        print(dic[rem],i)
        break
    dic[arr[i]] = i
    
print(dic)