s = "3[a2[c]]"
l = []
for i in s:
    if i != "]":
        l.append(i)
    else:
        char = ""
        while l[-1] != "[":
            char = l.pop() + char
        l.pop()
        num = ""
        while l and l[-1].isdigit():
            num = l.pop() + num
        l.append(char * int(num))
print("".join(l))