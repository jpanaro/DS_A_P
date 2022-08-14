# Basic implementation of binary search on a sorted array
# Takes specified array and target number
# Prints index of target number

def binary_search(arr, target):
    iteration_number = 0
    first_index = 0
    last_index = len(arr) - 1
    print("Starting array: " + str(arr))
    print("Target number: " + str(target))

    while (first_index <= last_index): # initial inclination, iterate as long as middle_index != target
        print("===================================================")
        print("Iteration number: " + str(iteration_number))
        iteration_number += 1
        # starting value is always at center of array
        middle_index = int((last_index + first_index)/2)
        print("\nCurrent middle index: " + str(middle_index))
        current_val = arr[middle_index]

        if current_val != target:
            print("Old array: " + str(arr[first_index:last_index+1])) # Must add 1 to last index or the last value gets chopped in the print
            if current_val < target:
                first_index = middle_index + 1
            else:
                last_index = middle_index - 1
            #print("first index = " + str(first_index))
            #print("last index = " + str(last_index))
            print("Adjusted new array: " + str(arr[first_index:last_index+1]))
        else:
            print("\n*******************************************")
            print("Search Concluded")
            print("Target number index: " + str(middle_index))
            print("Total Iterations: " + str(iteration_number))
            print("*******************************************")
            break # Could also say <first_index = last_index + 1> here instead of <break>

sample_array_1 = [1, 2, 3, 4, 5, 6, 7]

binary_search(sample_array_1, 1)

"""
# Array Addressing Reminder
a[start:stop]  # items start through stop-1
a[start:]      # items start through the rest of the array
a[:stop]       # items from the beginning through stop-1
a[:]           # a copy of the whole array
"""