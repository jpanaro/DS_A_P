from typing import List

def is_feasible(weights: List[int], max_weight: int, d: int) -> bool:
    days_required = 0
    capacity = max_weight
    sum_weight = 0
    i = 0
    n = len(weights)
    
    while (i < n):
        sum_weight += weights[i]
        if sum_weight > max_weight:
            days_required += 1
            i -= 1
            sum_weight = 0
        elif sum_weight == max_weight:
            days_required += 1
            sum_weight = 0
    if days_required <= d:
        return True
    else:
        return False

def min_max_weight(weights: List[int], d: int) -> int:
    left = max(weights)
    right = sum(weights)
    boundary = right
    
    while left <= right:
        mid = (left + right) // 2
        if is_feasible(weights, mid, d):
            boundary = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return boundary

if __name__ == '__main__':
    weights = [int(x) for x in input().split()]
    d = int(input())
    res = min_max_weight(weights, d)
    print(res)