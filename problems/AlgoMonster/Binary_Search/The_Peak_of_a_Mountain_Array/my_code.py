from typing import List

def peak_of_mountain_array(arr: List[int]) -> int:
    left = 0
    right = len(arr)-1
    boundary = -1
    
    while left <= right:
        mid = (left + right) // 2
        # edge case, no next element
        if mid == len(arr)-1:
            comp_val = float('-inf')
        else:
            comp_val = arr[mid+1]
        if arr[mid] > comp_val:
            boundary = mid
            right = mid - 1
        else:
            left = mid + 1
                
    return boundary

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    res = peak_of_mountain_array(arr)
    print(res)
