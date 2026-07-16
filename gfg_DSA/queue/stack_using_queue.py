queue = []

# Push
def push(x):
    queue.append(x)

    # Rotate the queue
    for i in range(len(queue) - 1):
        temp = queue.pop(0)
        queue.append(temp)

# Pop
def pop():
    if len(queue) == 0:
        return -1
    return queue.pop(0)

# Top
def top():
    if len(queue) == 0:
        return -1
    return queue[0]

# Size
def size():
    return len(queue)

def main():
    push(10)
    push(20)
    push(30)
    print(f"Top element: {top()}")
    print(f"Size of stack: {size()}")
    print(f"Popped element: {pop()}")
    print(f"Top element after pop: {top()}")
    print(f"Size of stack after pop: {size()}")
if __name__ == "__main__":
    main()