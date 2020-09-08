# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    left = 0
    right = 0
    current = 0

    while current < elements:
        if left < len(arrA) and right < len(arrB):
            if arrA[left] < arrB[right]:
                merged_arr[current] = arrA[left]
                left += 1
                current += 1

            else:
                merged_arr[current] = arrB[right]
                right += 1
                current += 1

        elif left < len(arrA):
            merged_arr[current] = arrA[left]
            left += 1
            current += 1

        elif right < len(arrB):
            merged_arr[current] = arrB[right]
            right += 1
            current += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr

    else:
        l = len(arr)//2
        arrA = merge_sort(arr[:l])
        arrB = merge_sort(arr[l:])
        arr = merge(arrA, arrB)

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

