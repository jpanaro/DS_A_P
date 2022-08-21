from typing import List

def find_first_occurrence(arr: List[int], target: int) -> int:
    left = 0
    right = len(arr)-1
    boundary = -1
    
    while (left <= right):
        mid_idx = (left + right) // 2
        mid_val = arr[mid_idx]
        if target == mid_val:
            boundary = mid_idx
        if target <= mid_val:
            right = mid_idx-1
        else:
            left = mid_idx+1
    return boundary

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = find_first_occurrence(arr, target)
    print(res)
