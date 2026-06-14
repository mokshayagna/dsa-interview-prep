"""
Input: arr = [1, 2, 4, 5, 7, 8, 3]
Output: true
Explanation: arr[5] = 8 is a peak element because arr[4] < arr[5] > arr[6].
    """
    
def find_peak_element(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        mid = (start + end)//2
        if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
            return True
        elif arr[mid - 1] < arr[mid] and arr[mid] < arr[mid + 1]:
            start = mid + 1
        else:
            end = mid - 1
    return True 

arr = [1, 2, 4, 5, 7, 8, 3]
result = find_peak_element(arr)
print("Is there a peak element in the array?", result)