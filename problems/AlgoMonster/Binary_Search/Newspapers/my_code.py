from typing import List


def is_feasible(newspapers_read_times: List[int], time_taken: int, num_coworkers: int) -> bool:
    min_time = time_taken
    i = 0
    n = len(newspapers_read_times)
    
    while i < n:
        # No more coworkers means no more reading newspapers, we stop here
        if num_coworkers == 0:
            return False
        if min_time - newspapers_read_times[i] > 0:
            min_time -= newspapers_read_times[i]
            i += 1
        elif min_time - newspapers_read_times[i] == 0:
            num_coworkers -= 1
            min_time = time_taken
            i += 1
        else: # We have a negative time taken (i.e. exceed the capacity)
            num_coworkers -= 1
            min_time = time_taken
     
    return True
        
    

def newspapers_split(newspapers_read_times: List[int], num_coworkers: int) -> int:
    min_time = max(newspapers_read_times)
    max_time = sum(newspapers_read_times)
    boundary = -1
    
    while (min_time <= max_time):
        mid_time = (min_time + max_time) // 2
        if is_feasible(newspapers_read_times, mid_time, num_coworkers):
            boundary = mid_time
            max_time = mid_time - 1
        else:
            min_time = mid_time + 1
            
    
    
    return boundary

if __name__ == '__main__':
    newspapers_read_times = [int(x) for x in input().split()]
    num_coworkers = int(input())
    res = newspapers_split(newspapers_read_times, num_coworkers)
    print(res)