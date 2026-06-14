"""
Input: n = 4
Output: 2
Explanation: Since, 4 is a perfect square, so its square root is 2.
"""
n = 11
def square_root(n):
    start = 0
    end = n
    ans = 0
    while start <= end:
        mid = (start + end) // 2
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
    return ans
result = square_root(n)
print("Square root of", n, "is:", result)