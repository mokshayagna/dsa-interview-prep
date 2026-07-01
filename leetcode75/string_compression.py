chars = ["a","a","b","b","c","c","c"]

res = []
i = 0
while i < len(chars):
    count = 1
    while i + 1 < len(chars) and chars[i] == chars[i + 1]:
        count += 1
        i += 1
    res.append(chars[i])
    if count > 1:
        if count > 10:
            for digit in str(count):
                res.append(digit)
        else:
            res.append(str(count))
    i += 1
print(res)