class heap:
    def __init__(self):
        self.heap = []
    
    def get_max(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]
    
    def extract_max(self):
        if len(self.heap) == 0:
            return None
        max_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.max_heapify(0)
        return max_value
    def max_heapify(self,i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != i:
            temp = self.heap[i]
            self.heap[i] = self.heap[largest]
            self.heap[largest] = temp
            self.max_heapify(largest)
def main():
    h = heap()
    h.heap = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("Max value:", h.get_max())
    print("Extracted max value:", h.extract_max())
    print("Max value after extraction:", h.get_max())
    print("Heap after extraction:", h.heap)

if __name__ == "__main__":
    main()