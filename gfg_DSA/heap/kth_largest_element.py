nums = [7, 10, 4, 3, 20, 15]
k = 3

def min_heapify(a,i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(a) and a[smallest] > a[left]:
            smallest = left
        if right < len(a) and a[smallest] > a[right]:
            smallest = right
        if smallest !=  i:
            a[i], a[smallest] = a[smallest], a[i]
            print(a)
            min_heapify(a,smallest)
            
def min_heap(a,n):
    for i in range(n//2-1,-1,-1):
        min_heapify(a,i)
    return a
    
def kth(a):
    for i in range(len(nums)):
        if a[0] < nums[i]:
            a[0] = nums[i]
        min_heapify(a,0)
    return a[0]
def main():
    a = []
    a = nums[:k]
    n = len(a)
    min_heap(a,n)
    print(f"kth largest element:{kth(a)}")
if __name__ == "__main__":
    main()