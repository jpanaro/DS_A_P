from typing import List

def find_boundary(arr: List[bool]) -> int:
    left_ptr = 0
    right_ptr = len(arr)-1
    
    if arr[0] == True:
        return 0
    
    while (left_ptr < right_ptr): # Without <= we miss single element edge case
        mid_idx = (right_ptr + left_ptr) // 2
        mid_val = arr[mid_idx]
        if mid_val == True:
            if arr[mid_idx-1] == False:
                return mid_idx
            else:
                right_ptr = mid_idx
        else:
            if arr[mid_idx+1] == True:
                return mid_idx+1
            else:
                left_ptr = mid_idx+1
    return -1
    

if __name__ == '__main__':
    arr = [x == "true" for x in input().split()]
    res = find_boundary(arr)
    print(res)
