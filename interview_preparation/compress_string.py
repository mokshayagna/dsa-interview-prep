chars = ["a","a","b","b","b","b","b","b","b","b","b","b","b","b"]

i = 0
t = []

while i < len(chars):
    count = 1   # include current char
    
    while i + 1 < len(chars) and chars[i] == chars[i+1]:
        count += 1
        i += 1
    
    t.append(chars[i])
    
    if count > 1:
        t.append(str(count))
    
    i += 1

print(t)

