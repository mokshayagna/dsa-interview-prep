a = "banana"
"""
Output:
    b:1
    a:3
    n:2
"""
dic = {}
for i in a:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
print(dic)