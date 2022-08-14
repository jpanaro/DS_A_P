from typing import List

def sort_list(unsorted_list: List[int]) -> List[int]:
    for index, value in enumerate(unsorted_list):
        min_val = float('inf')
        current = index
        while current < len(unsorted_list):
            if unsorted_list[current] < min_val:
                min_index = current
                min_val = unsorted_list[current]
            current += 1
        if min_index != current:
            unsorted_list[index], unsorted_list[min_index] = unsorted_list[min_index], unsorted_list[index]
               
    return unsorted_list

if __name__ == '__main__':
    unsorted_list = [int(x) for x in input().split()]
    res = sort_list(unsorted_list)
    print(' '.join(map(str, res)))