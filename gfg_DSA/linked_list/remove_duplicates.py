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
    
    def remove_duplicates(self):
        temp = self.head
        while temp.next is not None:
            if temp.data == temp.next.data:
                temp.next = temp.next.next
            else:
                temp = temp.next        
if __name__ == "__main__":
    ll = single_LL()
    ll.insert_at_beggining(10)
    ll.insert_at_beggining(10)
    ll.insert_at_beggining(10)
    ll.insert_at_beggining(20)
    ll.remove_duplicates()
    ll.printing()
    