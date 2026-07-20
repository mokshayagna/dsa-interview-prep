def max_heapify(arr,n,i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] >arr[largest]:
        largest = left
        
    if right < n and arr[right] > arr[largest]:
        largest = right
        
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)
def build_max_heap(arr,n):
    for i in range(n//2-1,-1,-1):
        max_heapify(arr,n,i)
def main():
    arr = [3,1,9,6,5,12,7,8,4,10]
    n = len(arr)
    build_max_heap(arr,n)
    print(arr)
if __name__ == "__main__":
    main()