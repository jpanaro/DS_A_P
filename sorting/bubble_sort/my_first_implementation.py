# Basic implementation of bubble sort algorithm for arrays
# Two 

def bubble_sort(arr):
    arr_length = len(arr)
    total_swaps = 0
    total_comparisons = 0
    total_iterations = 0
    print("\n\nLength of array: " + str(arr_length))
    print("Starting array: " + str(arr) + "\n")

    for i in range(arr_length): # for (int i=arr_lenth-1; i > 1; i--){}
        total_iterations += 1
        for j in range(arr_length-i-1): # for (int j=0; j<i; j++){}
            total_comparisons += 1
            if (arr[j] > arr[j+1]): 
                arr[j], arr[j+1] = arr[j+1], arr[j]
                total_swaps += 1
                print("Array at i=" + str(i) +" j=" + str(j) + ":\n" + str(arr))
            total_iterations += 1
    
    print("\n\nTotal Comparisons: " + str(total_comparisons))
    print("Total Swaps: " + str(total_swaps))
    print("Total Iterations: " + str(total_iterations))

sample_array_1 = [5, 1, 4, 2, 8] # Random Scenario

# Worst case scenario O(n^2) -> (n-1) + (n-2) + (n-3) +.....+ 1 = (n(n-1))/2 comparisons and swaps
# Outer loop iterates n times always, inner loop iterates (n(n-1))/2 times always
# Total number of iterations needed: (n-1)
sample_array_2 = [8, 5, 4, 2, 1] 
"""
n=3		Number of comparisons || Number of Swaps
[3, 2, 1]			0			    0
[2, 3, 1]			1			    1
[2, 1, 3]			2			    2
---------
[1, 2, 3]			3 			    3

Total Iterations = 2
"""

# Best Case scenario O(n) -> O(n) comparisons and O(1) swaps
# Outer loop iterates n times, inner loop iterates 0 times
sample_array_3 = [1, 2, 4, 5, 8]


sample_array_4 = [5, 1, 4, 2, 8, 3] # Random Scenario
sample_array_5 = [8, 5, 4, 3, 2, 1]  # Random Scenario

#bubble_sort(sample_array_1)
#bubble_sort(sample_array_2)
#bubble_sort(sample_array_3)
bubble_sort(sample_array_4)
bubble_sort(sample_array_5)