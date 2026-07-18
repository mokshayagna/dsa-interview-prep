class heap:
    def __init__(self):
        self.heap = []
        self.capacity = 10  # Set a default capacity for the heap
    
    def insert(self, value):
        if len(self.heap) == self.capacity:
            print("Heap is full. Cannot insert new value.")
            return
        self.heap.append(value)
        len(self.heap) + 1
        i = len(self.heap) - 1
        self.heap[i] = value
        
        while i != 0 and self.heap[(i - 1) // 2] < self.heap[i]:
            temp = self.heap[i]
            self.heap[i] = self.heap[(i - 1) // 2]
            self.heap[(i - 1) // 2] = temp
            i = (i - 1) // 2
def main():
    h = heap()
    h.insert(10)
    h.insert(20)
    h.insert(5)
    h.insert(15)
    print("Heap after insertions:", h.heap)
if __name__ == "__main__":
    main()