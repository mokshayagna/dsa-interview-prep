"""Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

    """
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class single_LL:
    def __init__(self):
        self.head = None
        
    def insert_at_beggining(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
    def printing(self):
        if self.head is None:
            print("Linkend List is empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data,end = "--->")
                temp = temp.next
    def length(self):
        if self.head is None:
            return 0
        else:
            temp = self.head
            count = 0
            while temp is not None:
                count += 1
                print(f" temp.next = {temp.next},temp.data = {temp.data} and  count = {count}")
                temp = temp.next
        print(f"Length of linked list is : {count}") 
        mid = count // 2
        print(f"Mid of linked list is : {mid}")
        temp = self.head
        for i in range(mid):
            temp = temp.next
        while temp is not None:
            print(temp.data,end = "--->")
            temp = temp.next
if __name__ == "__main__":
    ll = single_LL()
    ll.insert_at_beggining(60)
    ll.insert_at_beggining(50)
    ll.insert_at_beggining(40)
    ll.insert_at_beggining(30)
    ll.insert_at_beggining(20)
    ll.insert_at_beggining(10)
    ll.length()
    #ll.printing()