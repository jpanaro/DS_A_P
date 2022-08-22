def square_root(n: int) -> int:
    left = 0
    right = n-1
    boundary = -1
    
    while (left <= right):
        mid = (left + right) // 2
        root = mid * mid
        if root <= n:
            boundary = mid
            right = mid - 1
        else:
            left = mid + 1
    return boundary
            
        
if __name__ == '__main__':
    n = int(input())
    res = square_root(n)
    print(res)
