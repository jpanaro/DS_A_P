from typing import List

def binary_search(arr: List[int], target: int) -> int:
    left_ptr = 0
    right_ptr = len(arr)-1
    while (left_ptr != right_ptr):
        mid_idx = (right_ptr - left_ptr)
        mid_element = arr[mid_idx]
        if mid_element == target:
            return mid_idx
        elif mid_element > target:
            right_ptr = mid_idx-1
        else: # mid element < target
            left_ptr = mid_idx+1
    # One element left in array
    if arr[0] == target:
        return 0
    else:
        return -1
        

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = binary_search(arr, target)
    print(res)