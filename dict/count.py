a = [1,1,2,3,2]
dic = {}
for i in range(len(a)):
    if a[i] in dic:
        dic[a[i]] += 1
    else:
        dic[a[i]] = 1
print(dic)