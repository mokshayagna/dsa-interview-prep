class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List 1: 1 -> 3 -> 7
head1 = Node(1)
head1.next = Node(3)
head1.next.next = Node(7)

# Linked List 2: 2 -> 4 -> 8
head2 = Node(2)
head2.next = Node(4)
head2.next.next = Node(8)

# Linked List 3: 9
head3 = Node(9)

# Store the heads in an array
arr = [head1, head2, head3]

head1 = arr[0]
while head1:
    print(f"1st List: {head1.data} -> ", end="")
    head1 = head1.next

# Print all linked lists
for i in range(len(arr)):
    print(f"List {i + 1}: ", end="")
    temp = arr[i]
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("NULL")
    