"""
    Given an array, arr[] of non-negative integers. The task is to return the maximum of j - i (i<=j) subjected to the constraint of arr[i] <= arr[j].

Examples:
Input: arr[] = [34, 8, 10, 3, 2, 80, 30, 33, 1]
Output: 6
Explanation: In the given array arr[1] < arr[7] satisfying the required condition (arr[i] <= arr[j]) thus giving the maximum difference of j - i which is 7-1 = 6.
"""
arr = [34, 8, 10, 3, 2, 80, 30, 33, 1]

i = 0
j = len(arr)-1
ma = 0
while i < j:
    if arr[i] <= arr[j]:
        ma = max(ma,j-i)
        break
    elif arr[i] >= arr[j]:
        i += 1
        j -= 1
print(ma)
        