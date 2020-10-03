# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here

    # pointers for index of both arrays
    a_array_i = 0
    b_array_i = 0

    for i in range(elements):

        if a_array_i < len(arrA) and b_array_i < len(arrB):
            if arrA[a_array_i] <= arrB[b_array_i]:
                merged_arr[i] = arrA[a_array_i]
                a_array_i += 1
            else:
                merged_arr[i] = arrB[b_array_i]
                b_array_i += 1
        elif a_array_i < len(arrA) and b_array_i is len(arrB):
            merged_arr[i] = arrA[a_array_i]
            a_array_i += 1
        else:
            merged_arr[i] = arrB[b_array_i]
            b_array_i += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        center = len(arr) // 2
        left = arr[:center]
        right = arr[center:]
        left = merge_sort(left)
        right = merge_sort(right)
        return merge(left, right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

