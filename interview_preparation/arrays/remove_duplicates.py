n = 121
b = 0
while n != 0:
    a = n %10 # 1 #2
    b = b*10 + a
    n = n//10
print(b)