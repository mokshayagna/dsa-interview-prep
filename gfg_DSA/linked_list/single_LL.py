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
            
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        
    def insert_in_middle(self,data,place):
        new_node = Node(data)
        temp = self.head
        count = 1
        while temp is not None and count < place:
            temp = temp.next
            count += 1
        if temp is None:
            print("Invalid place")
        new_node.next = temp.next
        temp.next = new_node
        
        
    def delete_at_start(self):
        if self.head is None:
            print("LL in empty")
        self.head = self.head.next
    
    def delete_at_end(self):
        temp = self.head
        if self.head is None:
            print("LL is empty")
            return
        #if only one node
        if self.head.next is None:     
            self.head = None
        
        prev = None
        temp = self.head
        while temp.next is not None:
            prev = temp
            temp = temp.next
        prev.next = None

    def delete_by_place(self,place):
        temp = self.head
        prev = None
        count = 1
        while temp.next is not None and count < place:
            prev = temp
            temp = temp.next
            count += 1
        prev.next = temp.next
        temp.next = None
    
    def delete_by_value(self,value):
        if self.head is None:
            return
        if self.head.data == value:
            self.head = self.head.next
        
        prev = None
        temp = self.head
        while temp is not None:
            if temp.data == value:
                prev.next = temp.next
                return
            prev = temp
            temp = temp.next
                
            
    def printing(self):
        if self.head is None:
            print("Linkend List is empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data,end = "--->")
                temp = temp.next
        
if __name__ == "__main__":
    ll = single_LL()
    # ll.insert_at_beggining(10)
    # ll.insert_at_beggining(20)
    ll.insert_at_end(30)
    ll.insert_at_end(35)
    ll.insert_at_end(40)
    # ll.insert_in_middle(15,2)
    # ll.delete_at_start()
    # ll.delete_at_end()
    #ll.delete_by_place(2)
    ll.delete_by_value(35)
    ll.printing()
