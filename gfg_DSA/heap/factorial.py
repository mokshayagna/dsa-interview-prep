a = 5
i = 1
res = 1
while i <= a:
    res *= i
    i += 1
print(res)

def fact(a):
    if a == 1:
        return 1
    return a * fact(a-1)

print(fact(5))