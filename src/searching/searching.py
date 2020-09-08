# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    mid_point = (start + end) // 2

    if target <= end:

        if arr[mid_point] == target:
            return mid_point

        elif target < arr[mid_point]:
            left = mid_point - 1
            return binary_search(arr, target, start, left)

        else:
            right = mid_point + 1
            return binary_search(arr, target, right, end)

    else:
        return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
   # Your code here
   pass