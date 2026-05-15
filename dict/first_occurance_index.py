"""
a = [10, 5, 3, 4, 3, 5, 6]

Output: 5

Explanation:
    5 and 3 both repeat.
    First occurrence of 5 is at index 1.
    First occurrence of 3 is at index 2.
    Since 1 < 2, answer is 5.
"""
a = [10, 5, 3, 4, 3, 5, 6]
dic = {}
i = 0
j = len(a) - 1
for i in range(len(a)):
    if a[i] in dic:
        dic[a[i]]["count"] += 1
    else:
        dic[a[i]] = {
            "index" : i,
            "count": 1
        }
answer = -1
min_index = len(a)
for key, value in dic.items():
    if value["count"] > 1:
        if value["index"] < min_index:
            min_index = value["index"]
            answer = key
print(answer)