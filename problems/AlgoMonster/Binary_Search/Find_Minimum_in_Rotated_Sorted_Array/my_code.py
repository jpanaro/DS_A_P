from typing import List

def find_min_rotated(arr: List[int]) -> int:
    left = 0
    right = len(arr)-1
    boundary = -1
    last_num = arr[right]
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= last_num:
            boundary = mid
            right = mid - 1
        else:
            left = mid + 1
    return boundary

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    res = find_min_rotated(arr)
    print(res)