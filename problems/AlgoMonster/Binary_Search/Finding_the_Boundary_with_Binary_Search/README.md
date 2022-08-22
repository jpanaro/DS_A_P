# Finding the Boundary with Binary Search

## Problem Description

An array of boolean values is divided into two sections; the left section
consists of all false and the right section consists of all true. Find the
boundary of the right section, i.e. the index of the first true element. If
there is no true element, return -1.

## Example

Input: arr = [false, false, true, true, true]

Output: 2

Explanation: first true's index is 2.

## Intuition

This README was written too far after this problem was done so this section has
no content.

## Implementation

1. Establish left and right pointer variables to track iterations bounds.
2. Check if if the first value is True, if so we are done.
3. Iterate continuously over the array as long as the left pointer is not less
than the right pointer.
4. Calculate the middle index and grab the middle value.
5. If it is True, check if the value directly to the left is False and if so
return the current index. Otherwise set the right pointer equal to the middle
index.
6. If the middle index is False, check if the value directly to the right is
True and if so return the middle index + 1. Otherwise set the left pointer equal
to the middle index + 1.
7. If the while loop is exited, return -1 indicating no valid index was found.

## Complexity

### Time

Binary Search is O(log(n)) since we halve the number of values searched each
time.

### Space

Binary search has a space complexity of O(n).

## Notes

- ==If you need to find the "first", "minimum", "maximum" of a sorted array, boundary binary search is usually the key==
