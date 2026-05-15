a = [1,2,3,1,2]

dic = {}
for i in range(len(a)):
    if a[i] in dic:
        dic[a[i]] += 1
        print(a[i])
    else:
        dic[a[i]] = 1