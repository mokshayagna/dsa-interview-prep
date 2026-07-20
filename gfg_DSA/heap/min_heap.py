class min_heap:
    def __init__(self):
        self.a = []
    
    # will work only when the list already a min heap
    def get_min(self):
        if len(self.a) == 0:
            return None
        min_val = self.a[0]
        return min_val
    
    def extract_min_val(self):
        if len(self.a) == 0:
            return None
        min_val = self.a[0]
        self.a[0] = self.a[-1]
        self.a.pop()
        if len(self.a) > 0:
            self.min_heapify(0)
        return min_val
    def min_heapify(self,i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(self.a) and self.a[smallest] > self.a[left]:
            smallest = left
        if right < len(self.a) and self.a[smallest] > self.a[right]:
            smallest = right
        if smallest !=  i:
            self.a[i], self.a[smallest] = self.a[smallest], self.a[i]
            self.min_heapify(smallest)
    def min_heap(self):
        n = len(self.a)
        for i in range(n//2-1,-1,-1):
            self.min_heapify(i)
def main():
    h = min_heap()
    h.a = [9, 4, 7, 1, 3, 6, 2]
    # print("Min value:", h.get_min())
    # print("Extracted min value:", h.extract_min_val())
    h.min_heap()
    print("Min value after extraction:", h.get_min())
    print("Heap after extraction:", h.a)
    
if __name__ == "__main__":
    main()