# Square Root

## Problem Statement

Given an integer, find its square root without using the built-in square root function. Only return the integer part (truncate the decimals).

## Example

Input: 16

Output: 4

Input: 8

Output: 2

Explanation: square root of 8 is 2.83..., return integer part 2

## Intuition

Seeing as we could not take the square root outright I decided to "solve" the equation by redistributing the operation. Assume x = our given target number and y = the root. $$ \sqrt x = y \\ x = y^2$$ Unfortunately while my logic was sound I failed to update the pointers properly as I thought I would be able to follow similar rules from prior problems and update  the right pointer when our value of interest (a chosen y) was <= to x. This proved incorrect.

## Implementation

No valid implementation, revisit

## Complexity

### Time

Add when I complete a valid solution.

### Space

Add when I complete a valid solution.

## Notes

- Similar to previous problems we can break this down into a "True/False" array where we seek the boundary.

- ==Don't get stuck thinking all boundary problems require you to update the left and right pointers the same ways and in the same conditionals.==
