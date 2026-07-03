# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Empty list
        if head is None:
            return None

        # Only one node
        if head.next is None:
            return None

        l = []
        temp = head

        # Count nodes
        while temp is not None:
            l.append(temp.val)
            temp = temp.next

        middle = len(l) // 2

        prev = None
        temp = head
        count = 0

        while count < middle:
            prev = temp
            temp = temp.next
            count += 1

        # Delete middle node
        prev.next = temp.next
        temp.next = None

        return head