a = [5, 2, 8]
b = [10, 7, 12]
c = [9, 14, 6]
min_value = float('inf')
answer = []

"""
for i in range(len(a)):
    for j in range(len(b)):
        for k in range(len(c)):
            triplet = [a[i], b[j], c[k]]
            diff = max(triplet) - min(triplet)
            if diff < min_value:
                min_value = diff
                answer = triplet

print(sorted(answer))
"""
