# First Element Not Smaller than Target

## Problem Statement

Given an array of integers sorted in increasing order and a target, find the index of the first element in the array that is larger than or equal to the target. Assume that it is guaranteed to find a satisfying number.

## Example

Input:

arr = [1, 3, 3, 5, 8, 8, 10]
target = 2
Output: 1

Explanation: the first element larger than 2 is 3 which has index 1.

Input:

arr = [2, 3, 5, 7, 11, 13, 17, 19]
target = 6
Output: 3

Explanation: the first element larger than 6 is 7 which has index 3.

## Intuition

My immediate inclination was to implement a loop using `enumerate` and check the target against each value starting from index `0`. This was not an option as any solution had to include a binary search implementation so despite passing all tests I quickly abandoned this idea. Next, I figured I would be able to effectively mimic my solution for the "Finding the Boundary with Binary Search" problem but this quickly proved to be fruitless as my original implementation in that problem (while passing all relevant tests) was not scalable to other problems efficently. Ultimately I ran out of time before getting the correct solution.

## Implementation

No valid implementation, revisit.

## Complexity

### Time

Add when I complete a valid solution.

### Space

Add when I complete a valid solution.

## Notes

Similar to previous problems we can break this down into a "True/False" array where we seek the boundary.

The proper solution involved implementing an extra value titled `boundary`. We keep a variable `boundary` that represents the leftmost true's index currently recorded. If the current element is true, then we update boundary_index with its index and discard everything to the right including the current element itself since its index has been recorded by the variable.
