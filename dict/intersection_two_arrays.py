a = [1,2,2,1]
b = [2,2]
"""
Output:
    [2,2]
""" 
dic = {}
output = []
for i in range(len(a)):
    if a[i] in dic:
        dic[a[i]] += 1
    else:
        dic[a[i]] = 1
for num in b:
    if num in dic and dic[num]>0:
        output.append(num)
print(output)