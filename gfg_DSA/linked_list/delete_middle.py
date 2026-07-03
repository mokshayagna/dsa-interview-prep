class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class single_LL:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
    
    def printing(self):
        if self.head is None:
            print("Linkend List is empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data,end = "--->")
                temp = temp.next
                
    def delete_middle(self):
        l = []
        temp = self.head
        while temp is not None:
            l.append(temp.data)
            temp = temp.next
        middle = len(l) // 2
        count = 1
        prev = None
        temp = self.head
        while temp.next is not None and count < middle+1:
            prev = temp
            temp = temp.next
            count += 1
        prev.next = temp.next
        temp.next = None
            
            
if __name__ == "__main__":
    ll = single_LL()
    ll.insert_at_end(2)
    ll.insert_at_end(1)
    # ll.insert_at_end(3)
    # ll.insert_at_end(4)
    # ll.insert_at_end(7)
    # ll.insert_at_end(1)
    # ll.insert_at_end(2)
    # ll.insert_at_end(6)
    ll.delete_middle()
    ll.printing()