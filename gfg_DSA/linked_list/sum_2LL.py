class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# First Linked List: 1 -> 2 -> 3
head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(3)

# Second Linked List: 9 -> 9 -> 9
head2 = Node(9)
head2.next = Node(9)
head2.next.next = Node(9)


# Print First Linked List
print("First Linked List:")
temp = head1
while temp:
    print(temp.data, end=" ")
    temp = temp.next
print()

# Print Second Linked List
print("Second Linked List:")
temp = head2
while temp:
    print(temp.data, end=" ")
    temp = temp.next
print()

# Convert linked lists to numbers
temp1 = head1
temp2 = head2

num1 = ""
num2 = ""

while temp1:
    num1 = num1 + str(temp1.data)
    temp1 = temp1.next

while temp2:
    num2 = num2 + str(temp2.data)
    temp2 = temp2.next

print(f"num1 = {num1} and num2 = {num2}")

sum_of_num = int(num1) + int(num2)
print(f"sum_of_num = {sum_of_num}")

# Convert sum to linked list
digits = str(sum_of_num)

head3 = Node(int(digits[0]))
temp = head3

for digit in digits[1:]:
    temp.next = Node(int(digit))
    temp = temp.next

# Print the resulting linked list
print("Sum as Linked List:")
temp = head3
while temp:
    print(temp.data, end=" ")
    temp = temp.next
print()