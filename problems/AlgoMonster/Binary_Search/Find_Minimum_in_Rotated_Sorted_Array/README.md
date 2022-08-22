# Find Minimum in Rotated Sorted Array

## Problem Description

A sorted array of unique integers was rotated at an unknown pivot. For example, [10, 20, 30, 40, 50] becomes [30, 40, 50, 10, 20]. Find the index of the minimum element in this array. All the numbers are unique.

## Example

Input: [30, 40, 50, 10, 20]

Output: 3

Explanation: the smallest element is 10 and its index is 3.

Input: [3, 5, 7, 11, 13, 17, 19, 2]

Output: 7

Explanation: the smallest element is 2 and its index is 7.

## Intuition

First I wanted to try and base my algorithm around the surronging elements of the mid element when it was chosen. For examples check if mid+1 and mid-1 were bigger or smaller than mid and proceed from there. It quickly became apparent that this was not a sustainable solution as the information extracted was insufficent to update the left and right pointers accurately. Next, I wanted to find a way to split the elements into two True and False groups based on a criteria. What I chose was to make the groups based on whether or not the number was greater or less than the last element in the array. This way we could effectively update the left and right pointers.

## Implementation

Program a typical boundary binary search and also add a static variable to track the last number value in the array. If the mid value is <= last value set the boundary equal to the mid index and change the right pointer to mid index + 1. If it is > last value change the left pointer to mid index + 1. Once the left pointer is >= the right pointer return the boundary value.

## Complexity

### Time

O(log(n))

### Space

O(n)

## Notes

- ==Always look for a way to "convert" the input array into two sequential groups of True and False with a boundary. You may have to get creative.==

- ==Binary search can work beyond sorted arrays, as long as there is a binary decision we can use to shrink the search range.==

- Visualizing the input array may help you uncover a path forward.
