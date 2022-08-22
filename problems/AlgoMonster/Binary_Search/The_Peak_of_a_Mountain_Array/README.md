# First Element Not Smaller than Target

## Problem Statement

A mountain array is defined as an array that

has at least 3 elements
has an element with the largest value called "peak", with index k. The array elements monotonically increase from the first element to A[k], and then monotonically decreases from A[k + 1] to the last element of the array. Thus creating a "mountain" of numbers.
That is, given A[0]<...<A[k-1]<A[k]>A[k+1]>...>A[n-1], we need to find the index k. Note that the peak element is neither the first nor the last element of the array.

Find the index of the peak element. Assume there is only one peak element.

## Example

Input: 0 1 2 3 2 1 0

Output: 3

Explanation: the largest element is 3 and its index is 3.

## Intuition

Here, I could immediately see this was another boundary problem and could be treated as a True/False array. The two cases I knew we needed to account for were if the mid_val+1 was > the mid_val or not. From there I would be able to eliminate half the choices as all proceeding values would either be bigger or smaller. I also knew if we happened to be on the last index of the array we would get an out-of-bounds error so I accounted for that.

## Implementation

Implement a typical boundary binary search but add a conditonal for having a mid_index on the very end of the array. Also, the comparison is between arr[mid] and arr[mid+1]. If arr[mid] is bigger than it's neighbor then you move the right pointer to mid-1 since all values past mid+1 are guaranteed to be smaller, and if arr[mid] is smaller the left pointer is moved to mid+1 since all values past mid+1 are guaranteed to be greater (and include the peak).

## Complexity

### Time

O(log(n))

### Space

O(n)

## Notes

- Similar to previous problems we can break this down into a "True/False" array where we seek the boundary.

- Keep an eye out for edge cases (especially with accessing comparison indices).
