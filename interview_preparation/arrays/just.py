arr = [1,2,3,4,5]
k = 3

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

rev = []
rev = arr[0:k] + arr[len(arr):k:-1]
print(rev)