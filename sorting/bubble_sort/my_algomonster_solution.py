from typing import List

def sort_list(unsorted_list: List[int]) -> List[int]:
    n = len(unsorted_list)
    for i in reversed(range(n)):
        for j in range(i):
              if unsorted_list[j] > unsorted_list[j+1]:
                  unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
               
    return unsorted_list

if __name__ == '__main__':
    unsorted_list = [int(x) for x in input().split()]
    res = sort_list(unsorted_list)
    print(' '.join(map(str, res)))
