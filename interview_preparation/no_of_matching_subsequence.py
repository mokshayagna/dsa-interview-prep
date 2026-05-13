s = "abcde"
words = ["a","bb","acd","ace"]
#output = 3
i = 0
count = 0
for word in words:
    j = 0
    for char in s:
        if j < len(word) and char == word[j]:
            j += 1
    if j == len(word):
        count += 1
print(count)