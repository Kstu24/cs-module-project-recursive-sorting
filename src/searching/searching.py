# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here

    if len(arr) == 0:
        return -1
    
    center = (start + end) // 2

    if start == end:
        return -1
    
    if target == arr[center]:
        return center
    
    if target > arr[center]:
        start = center
        return binary_search(arr, target, start, end)
    
    if target < arr[center]:
        end = center
        return binary_search(arr, target, start, end)

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
