"""Given an array arr[] of integers, where each element arr[i] represents the number of pages in the 
i-th book. You also have an integer k representing the number of students. 
The task is to allocate books to each student such that:

        Each student receives atleast one book.
        Each student is assigned a contiguous sequence of books.
        No book is assigned to more than one student.
        All books must be allocated.
The objective is to minimize the maximum number of pages assigned to any student. 
In other words, out of all possible allocations, find the arrangement where the student who receives 
the most pages still has the smallest possible maximum.
    """

def is_valid(arr, n, m, max_pages):
    student= 1
    pages = 0
    for i in range(n):
        if arr[i] > max_pages:
            return False
        if pages + arr[i] <= max_pages:
            pages += arr[i]
        else:
            student += 1
            pages = arr[i]
    if student > m:
        return False
    return True
def allocate(arr,n,m):
    if(m>n):
        return -1
    ans = 0
    start = 0
    end = sum(arr)
    while start < end:
        mid = (start + end) // 2
        if is_valid(arr, n, m, mid):
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    return ans
def main():
    arr = [22,23,67]      
    m = 1
    n = len(arr) 
    result = allocate(arr, n, m)
    print("Minimum number of pages allocated to a student:", result)
if __name__ == "__main__":    
    main()