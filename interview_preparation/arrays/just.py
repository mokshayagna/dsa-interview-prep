# arr = [1,2,3,4,5]
# k = 3

"""Reverse whole array"""

 # print(arr[::-1])

""" Reverse 1st k elements
    """
# n = len(arr)
# rev = []
# rev = arr[0:k+1][::-1] + arr[k+1:n]
# print(rev)

"""Reverse last k elements
o/p = [1,2,5,4,3]
    """

# arr = [1,2,3,4,5]
# k = 3

# rev = arr[:-k] + arr[-k:][::-1]
# print(rev)

"""
    Extract Middle Portion

Input : arr = [1,2,3,4,5,6,7]

Output : [3,4,5]
    """
# arr = [1,2,3,4,5,6,7]
# print(arr[2:5])

"""Left Rotate by K

Input :[1,2,3,4,5]
k = 2

Output : [3,4,5,1,2]
    """
# arr = [1,2,3,4,5]
# k = 2
# print(arr[k:] + arr[:k])

"""
    Right Rotate by K

Input : [1,2,3,4,5]
k = 2

Output : [4,5,1,2,3]
    """
# arr = [1,2,3,4,5]
# k = 2

# print(arr[k+1:] + arr[:k+1])

"""
    Move First Element to End

Input

[1,2,3,4]

Output : [2,3,4,1]
    """

# arr = [1,2,3,4]
# print(arr[1:] + arr[:1])

"""
Move Last Element to Front
Input:[1,2,3,4]

Output:[4,1,2,3]
    """
# arr = [1,2,3,4]

# print(arr[-1:]+arr[:-1])

"""Reverse Between Two Indices

Input
arr = [1,2,3,4,5,6]
l = 1
r = 4

Output
[1,5,4,3,2,6]
    """
# arr = [1,2,3,4,5,6]
# l = 1
# r = 4
# res = []
# res = arr[:l] + arr[r:l-1:-1] + arr[-1:]    
# print(res)

"""
Reverse Every Group of K
Input:[1,2,3,4,5,6,7,8]
k = 3

Output:[3,2,1,6,5,4,8,7]
"""

# arr = [1,2,3,4,5,6,7,8]
# k = 3
# rev = []
# for i in range(0,len(arr)-1,k):
#     rev.extend(arr[i:i+k][::-1])
# print(rev)

"""
Maximum consecutive one’s (or zeros) in a binary array
Input: arr[] = [0, 1, 0, 1, 1, 1, 1]
Output: 4
Explanation: The maximum number of consecutive 1’s in the array is 4 from index 3-6.

Input: arr[] = [0, 0, 1, 0, 1, 0]
Output: 2
Explanation: The maximum number of consecutive 0’s in the array is 2 from index 0-1.
    """
# arr = [0, 1, 0, 1, 1, 1, 1]
# count = 0
# max_count = 0
# for i in range(len(arr)):
#     if arr[i] == arr[i-1]:
#         count += 1
#     else:
#         max_count = max(count,max_count)
#         count = 1
# print(max(max_count,count))

"""Move all Zeros to End of Array
nput: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
Output: [1, 2, 4, 3, 5, 0, 0, 0]
Explanation: There are three 0s that are moved to the end.
    """
    
arr = [1, 2, 0, 4, 3, 0, 5, 0]
i = 0
r = len(arr)-1
while i < r:
    if arr[i] == 0:
        arr.append(arr.pop(i))
        r -= 1
    i += 1
print(arr)