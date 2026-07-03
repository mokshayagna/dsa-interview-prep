# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        temp = head
        l = []
        while temp is not None:
            l.append(temp)
            temp = temp.next
        for i in range(len(l)-1,0,-1):
            l[i].next = l[i-1]
        l[0].next = None
        return l[-1]