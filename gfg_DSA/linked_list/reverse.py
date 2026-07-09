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

    # def reverse(self):
    #     if self.head is None:
    #         return
    #     l = []
    #     temp = self.head
    #     while temp is not None:
    #         l.append(temp)
    #         temp = temp.next
    #     for i in range(len(l)-1, 0, -1):
    #         l[i].next = l[i-1]

    #     l[0].next = None
    #     self.head = l[-1]
    
    def reverse(self):
        if self.head is None:
            return
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        
if __name__ == "__main__":
    ll = single_LL()
    ll.insert_at_beggining(10)
    ll.insert_at_beggining(20)
    ll.insert_at_beggining(30)
    ll.insert_at_beggining(40)
    ll.printing()
    ll.reverse()
    ll.printing()