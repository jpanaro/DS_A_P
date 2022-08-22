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

My immediate inclination (similar to the previous problem "First Element Not Smaller than Target") was to implement a loop using `enumerate` and check the target against each value starting from index `0`. Like before this is not a valid solution. Now that I had knowledge of how to implement a binary search with boundary properly I decided to pursue that course with a minor adjustment detailed below.

## Implementation

This solution involves a vanilla binary search implementation with an extra variable `boundary` that represents the leftmost true's index currently recorded. If the current element is true, then we update `boundary` with its index and discard everything to the right including the current element itself since its index has been recorded by the variable. Here, we only updated `boundary` if our current value of interest was equivalent to out target. Otherwise we just updated the left and right pointer variables like normal.

## Complexity

### Time

O(log(n))

### Space

O(n)

## Notes

Similar to previous problem "First Element Not Smaller than Target" we can break this down into a "True/False" array where we seek the boundary. The differentiatior is explained in the "Implementation" section above.
