s1 = []
s2 = []
"""
Enqueue operation of queue using 2 stacks
    """
s1.append(10)
s1.append(20)

"""
Dequeue operation of queue using 2 stacks
    """
print(f"S1: {s1}")
while len(s1) != 0:
    s2.append(s1.pop())
ans = s2.pop()
while len(s2) != 0:
    s1.append(s2.pop())
print(f"Dequeued element: {ans}")
print(f"S1: {s1}")