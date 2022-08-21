# First Element In Sorted Array with Duplicates

## Problem Statement

Given a sorted array of integers and a target integer, find the first occurrence of the target and return its index. Return -1 if the target is not in the array.

## Example

Input:

arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
target = 3
Output: 1

Explanation: First occurrence of 3 is at index 1.

Input:

arr = [2, 3, 5, 7, 11, 13, 17, 19]
target = 6
Output: -1

Explanation: 6 does not exists in the array.

## Intuition

My immediate inclination was to implement a loop using `enumerate` and check the target against each value starting from index `0`. This was not an option as any solution had to include a binary search implementation so despite passing all tests I quickly abandoned this idea. Next, I figured I would be able to effectively mimic my solution for the "Finding the Boundary with Binary Search" problem but this quickly proved to be fruitless. Ultimately I ran out of time before getting the correct solution.

## Implementation

No valid implementation, revisit

## Complexity

### Time

Add when I complete a valid solution.

### Space

Add when I complete a valid solution.

## Notes

Similar to previous problems we can break this down into a "True/False" array where we seek the boundary.

The proper solution involved implementing an extra value titled `boundary`. We keep a variable `boundary` that represents the leftmost true's index currently recorded. If the current element is true, then we update boundary_index with its index and discard everything to the right including the current element itself since its index has been recorded by the variable.
